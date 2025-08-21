from playwright.sync_api import sync_playwright


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    context = browser.new_context(storage_state='.auth/otaku.json')

    page = context.new_page()
    page.goto('https://otaku.bg/', wait_until='networkidle')

    page.click('span.ts-wpop-tab[data-range="monthly"]', timeout=10000)

    top_anime_list = page.locator('div.serieslist.pop.wpop.wpop-monthly div.leftseries a.series')

    for i in range(top_anime_list.count()):
        title = top_anime_list.nth(i).inner_text()
        url = top_anime_list.nth(i).get_attribute("href")

        print(f"{i+1}. {title}: {url}")

    browser.close()