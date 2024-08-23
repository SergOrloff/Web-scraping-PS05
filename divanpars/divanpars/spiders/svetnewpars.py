import scrapy

class SvetnewparsSpider(scrapy.Spider):
    # Название паука
    name = "svetnewpars"

    # Ограничение доменов, которые паук может обрабатывать
    allowed_domains = ["https://divan.ru"]

    # Начальные URL-адреса для паука
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        # Убедитесь, что CSS-селектор соответствует элементам, которые вы хотите собрать
        svets = response.css('div._Ud0k')

        for svet in svets:
            # Сбор данных для каждого элемента
            yield {
                'name': svet.css('div.lsooF span::text').get(),  # Извлечение названия светильника
                'price': svet.css('div.pY3d2 span::text').get(),  # Извлечение цены светильника
                'url': response.urljoin(svet.css('a::attr(href)').get())
                # Формирование полного URL с использованием urljoin для обработки относительных ссылок
            }

        # Пагинация: переход на следующую страницу, если она существует
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)  # Следуем за ссылкой на следующую страницу и продолжаем обработку