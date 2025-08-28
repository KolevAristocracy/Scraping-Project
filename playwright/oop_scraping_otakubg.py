import time

from playwright.sync_api import sync_playwright


class OtakuScraper:
    def __init__(self, auth_file='.auth/otaku.json', headless=True):
        self.auth_file = auth_file
        self.headless = headless
        self.browser = None
        self.context = None
        self.page = None

    def __enter__(self):
        self.pw = sync_playwright().start()
        self.browser = self.pw.chromium.launch(headless=self.headless)
        self.context = self.browser.new_context(storage_state=self.auth_file)
        self.page = self.context.new_page()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.browser.close()
        self.pw.stop()

    def open_homepage(self, url='https://otaku.bg/'):
        self.page.goto(url, wait_until='networkidle')

    def click_monthly_tab(self):
        self.page.click('span.ts-wpop-tab[data-range="monthly"]', timeout=10000)

    def scrape_list(self, selector: str, limit: int = 10):
        locator = self.page.locator(selector)
        results = []

        for i in range(min(locator.count(), limit)):
            title = locator.nth(i).inner_text()
            url = locator.nth(i).get_attribute("href")
            results.append((title, url))
        return results

    def get_top_anime(self, limit: int = 5):
        selector = 'div.serieslist.pop.wpop.wpop-monthly div.leftseries a.series'
        return self.scrape_list(selector, limit)

    def get_recent_releases(self, limit=10):
        selector = 'span.ts-ajax-cache div.leftseries a.series'
        return self.scrape_list(selector, limit)

if __name__ == "__main__":
    with OtakuScraper() as scraper:
        scraper.open_homepage()
        scraper.click_monthly_tab()

        top = scraper.get_top_anime()
        recent = scraper.get_recent_releases()
        print(f"Мost up-to-date information as of today: {time.asctime()}")
        print("Top 5 most popular for the month:\n")
        for i, (title, url) in enumerate(top, 1):
            print(f"{i}. {title}: {url}")

        print("\nMost Recent Releases:\n")
        for i, (title, url) in enumerate(recent, 1):
            print(f"{i}. {title}: {url}")


