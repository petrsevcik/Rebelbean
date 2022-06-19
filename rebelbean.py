from playwright.sync_api import sync_playwright

RB_URL = "https://www.rebelbean.cz"


def rb_scraper():
    result = ()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"{RB_URL}/kava/")
        all_coffee = page.query_selector_all('.product')
        for coffee in all_coffee:
            name = coffee.query_selector('.name').inner_text()
            status = coffee.query_selector('.availability').inner_text()
            link = coffee.query_selector("a").get_attribute("href")
            _price = coffee.query_selector("strong").inner_text()
            price = int("".join([i for i in _price if i.isdigit()]))
            print({'coffee': name, 'status': status, "link": link, "price": price})
            if name == "TEST ROAST":
                result = (name, status, link, price)
        browser.close()
        if not result:
            print("Test roast not found")
            return False
        if result[1] == "Vyprodáno":
            print("Test roast sold out!")
            return False
        return result


def test_roast_scraper():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        test_roast_url = f"{RB_URL}/test-roast/"
        page.goto(test_roast_url)
        page.locator("//*[@id='parameter-id-227']/label[1]/span[1]").click()  # click "Klasická produkce"
        availability_status = page.locator("//*[@id='product-detail-form']/div[2]/div[1]/div[1]/span[1]/span")
        availability = availability_status.inner_text().strip()
        _price = page.locator("//*[@id='product-detail-form']/div[2]/div[2]/strong/span").inner_text()
        price = int("".join([i for i in _price if i.isdigit()]))
        if availability == "vyprodáno":
            print("Test roast sold out!")
            return False
        else:
            result = (availability, price, test_roast_url)
            return result


def main_scraper():
    try:  # main scraper
        result = rb_scraper()
        if result:
            print("Test roast available")
            price = result[3]
            link = f"{RB_URL}{result[2]}"
            if test_roast_scraper():
                print(f"Caffeine version available for {price} CZK. Order here: {link}")
                return result
        return False
    except:  # backup
        result = test_roast_scraper()
        if result:
            price = result[1]
            link = result[2]
            print(f"Caffeine version available for {price} CZK. Order here: {link}")
            return result
        return False


if __name__ == "__main__":
    main_scraper()
