import requests
import bs4
import collections


WeatherReport = collections.namedtuple(
    'WeatherReport', 'cond, temp, scale, loc')


def main():
    print_header()

    code = input('What zipcode do you want to weather for (97201)? ')

    html = get_html_from_code(code)

    report = get_weather_from_html(html)

    report_weather(report)


def print_header():
    print('WEATHER APP')
    print('============')


def get_html_from_code(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)

    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    header = soup.find(class_='region-content-header')

    if not header:
        return None

    loc = header.find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(
        class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(
        class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc.split('\n')[0].strip())
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    return WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)


def cleanup_text(text: str):
    return text if not text else text.strip()


def report_weather(report):
    if report:
        print('The temp in {} is {} {} and {}'.format(
            report.loc,
            report.temp,
            report.scale,
            report.cond
        ))
    else:
        print('Wrong zipcode 😟')


if __name__ == '__main__':
    main()
