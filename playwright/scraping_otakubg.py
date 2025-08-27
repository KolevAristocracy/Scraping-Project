from playwright.sync_api import sync_playwright


def top_monthly_result(page, limit=10):
    page.click('span.ts-wpop-tab[data-range="monthly"]', timeout=10000)
    locator = 'div.serieslist.pop.wpop.wpop-monthly div.leftseries a.series'

    return scrape_anime_list(page, locator, limit)

def most_recent_releases(page, limit=5):
    locator = 'span.ts-ajax-cache div.leftseries a.series '
    return scrape_anime_list(page, locator, limit)


def scrape_anime_list(page, selector: str, limit: int):
    locator = page.locator(selector)
    results = []

    for i in range(min(locator.count(), limit)):
        title = locator.nth(i).inner_text()
        url = locator.nth(i).get_attribute("href")
        results.append((title, url))
    return results


def initial_scraper():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context(storage_state='.auth/otaku.json')

        page = context.new_page()
        page.goto('https://otaku.bg/', wait_until='networkidle')

        top_anime = top_monthly_result(page)
        recent_releases = most_recent_releases(page)

        browser.close()
        return top_anime, recent_releases


def print_results():
    top, recent = initial_scraper()
    print("Top 5 most popular for the month:\n")
    for i, (title, url) in enumerate(top, 1):
        print(f"{i}. {title}: {url}")

    print("\nMost Recent Releases:\n")
    for i, (title, url) in enumerate(recent, 1):
        print(f"{i}. {title}: {url}")


if __name__ == "__main__":
    print_results()
