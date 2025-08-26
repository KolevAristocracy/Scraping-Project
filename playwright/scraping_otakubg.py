from playwright.sync_api import sync_playwright


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    context = browser.new_context(storage_state='.auth/otaku.json')

    page = context.new_page()
    page.goto('https://otaku.bg/', wait_until='networkidle')

    page.click('span.ts-wpop-tab[data-range="monthly"]', timeout=10000)

    top_anime_list = page.locator('div.serieslist.pop.wpop.wpop-monthly div.leftseries a.series')
    recent_releases = page.locator('span.ts-ajax-cache div.leftseries a.series ')

    print("Top 5 most popular for the month:\n")
    for i in range(top_anime_list.count()):


        title = top_anime_list.nth(i).inner_text()
        url = top_anime_list.nth(i).get_attribute("href")

        print(f"{i+1}. {title}: {url}")

    print("\nMost Recent Releases:\n")
    for i in range(recent_releases.count()):

        title = recent_releases.nth(i).inner_text()
        url = recent_releases.nth(i).get_attribute("href")

        print(f"{i+1}. {title}: {url}")

    browser.close()