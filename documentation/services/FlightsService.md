# FlightsService

A list of all methods in the `FlightsService` service. Click on the method name to view detailed information about that method.

| Methods                                     | Description         |
| :------------------------------------------ | :------------------ |
| [flights_home](#flights_home)               | Flights Home        |
| [flights_day_view](#flights_day_view)       | Flights Day View    |
| [calendar_month_view](#calendar_month_view) | Calendar Month View |
| [multi_city](#multi_city)                   | Multi-City          |
| [browse_view](#browse_view)                 | Browse View         |
| [cheap_flights_to](#cheap_flights_to)       | Cheap Flights To    |
| [flights_airline](#flights_airline)         | Flights Airline     |

## flights_home

Flights Home

- HTTP Method: `GET`
- Endpoint: `/g/referrals/v1/flights/home/`

**Parameters**

| Name             | Type | Required | Description                                    |
| :--------------- | :--- | :------- | :--------------------------------------------- |
| media_partner_id | str  | ❌       | Your Impact partner ID as found at Impact.com. |

**Example Usage Code Snippet**

```python
from skyscanner_referrals import SkyscannerReferrals, Environment

sdk = SkyscannerReferrals(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.flights.flights_home(media_partner_id="{{mediaPartnerId}}")

print(result)
```

## flights_day_view

Flights Day View

- HTTP Method: `GET`
- Endpoint: `/g/referrals/v1/flights/day-view/`

**Parameters**

| Name                    | Type | Required | Description                                                                                                                                                                    |
| :---------------------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| media_partner_id        | str  | ❌       | Your Impact partner ID as found on impact.com.                                                                                                                                 |
| origin                  | str  | ❌       | IATA code or Entity ID for the origin.                                                                                                                                         |
| destination             | str  | ❌       | IATA code or Entity ID for the destination.                                                                                                                                    |
| outbound_date           | str  | ❌       | Outbound date in the format YYYY-MM-DD.                                                                                                                                        |
| inbound_date            | str  | ❌       | Inbound date in the format YYYY-MM-DD.                                                                                                                                         |
| utm_term                | str  | ❌       | Additional alphanumeric tracking parameter you can add to your text links for additional tracking. This will be reported on Impact as Sub Id 2.                                |
| adultsv2                | str  | ❌       | Number of adult passengers. Adults have to be 16 years old or older.                                                                                                           |
| childrenv2              | str  | ❌       | Number of children passengers. Child age has to be in the 2-15 range. The value must be in the format integer\|integer... where each number is the age of the child passenger. |
| infants                 | str  | ❌       | Number of infant passengers. An infant is 1 year old or younger.                                                                                                               |
| cabinclass              | str  | ❌       | Cabin class for the flight.                                                                                                                                                    |
| prefer_directs          | str  | ❌       | When this parameter is set to true, only direct flights results will be shown.                                                                                                 |
| outboundaltsenabled     | str  | ❌       | When this parameter is set to true, the results will include nearby airports as an outbound place.                                                                             |
| inboundaltsenabled      | str  | ❌       | When this parameter is set to true, the results will include nearby airports as an inbound place.                                                                              |
| alternativeorigins      | str  | ❌       | An array of location codes which will be used as alternative origins.                                                                                                          |
| alternativedestinations | str  | ❌       | An array of location codes which will be used as alternative destinations.                                                                                                     |
| market                  | str  | ❌       | The preferred market for searching results. When unspecified, we use detection logic to determine the market, so it is unlikely you will need to use this parameter.           |
| locale                  | str  | ❌       | The preferred locale for the desired page. When unspecified, we use detection logic to determine the locale, so it is unlikely you will need to use this parameter.            |
| currency                | str  | ❌       | The preferred currency for the desired page. When unspecified, we use detection logic to determine the currency, so it is unlikely you will need to use this parameter.        |
| sortby                  | str  | ❌       | Sets the sorting order for the results. If not specified, results will be sorted by best.                                                                                      |
| airlines                | str  | ❌       | Comma separated list of IATA/ICAO airline codes to be passed to the day-view filters.                                                                                          |
| alliances               | str  | ❌       | Comma separated list of alliance names passed to the day-view filters.                                                                                                         |
| departure_times         | str  | ❌       | Sets the day-view departure time filters in minutes.                                                                                                                           |
| duration                | str  | ❌       | Sets the day-view duration filters in minutes.                                                                                                                                 |

**Example Usage Code Snippet**

```python
from skyscanner_referrals import SkyscannerReferrals, Environment

sdk = SkyscannerReferrals(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.flights.flights_day_view(
    media_partner_id="{{mediaPartnerId}}",
    origin="CDG",
    destination="EDI",
    outbound_date="{{outbounddate}}",
    inbound_date="{{inbounddate}}",
    utm_term="summer",
    adultsv2="2",
    childrenv2="3|4",
    infants="1",
    cabinclass="premiumeconomy",
    prefer_directs="true",
    outboundaltsenabled="true",
    inboundaltsenabled="true",
    alternativeorigins="BCN,LIS",
    alternativedestinations="BCN,LIS",
    market="FR",
    locale="fr-FR",
    currency="EUR",
    sortby="fastest",
    airlines="AF,EZY,TK",
    alliances="OneWorld,SkyTeam",
    departure_times="00-90,30-990",
    duration="1320"
)

print(result)
```

## calendar_month_view

Calendar Month View

- HTTP Method: `GET`
- Endpoint: `/g/referrals/v1/flights/calendar-month-view/`

**Parameters**

| Name             | Type | Required | Description                                                                                                                                     |
| :--------------- | :--- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| media_partner_id | str  | ❌       | Your Impact partner ID as found on impact.com.                                                                                                  |
| origin           | str  | ❌       | IATA code or Entity ID for the origin.                                                                                                          |
| destination      | str  | ❌       | IATA code or Entity ID for the destination.                                                                                                     |
| prefer_directs   | str  | ❌       | If set to true, only direct flights will be shown as results.                                                                                   |
| utm_term         | str  | ❌       | Additional alphanumeric tracking parameter you can add to your text links for additional tracking. This will be reported on Impact as Sub Id 2. |

**Example Usage Code Snippet**

```python
from skyscanner_referrals import SkyscannerReferrals, Environment

sdk = SkyscannerReferrals(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.flights.calendar_month_view(
    media_partner_id="{{mediaPartnerId}}",
    origin="CDG",
    destination="EDI",
    prefer_directs="true",
    utm_term="summer"
)

print(result)
```

## multi_city

Multi-City

- HTTP Method: `GET`
- Endpoint: `/g/referrals/v1/flights/multicity/`

**Parameters**

| Name             | Type | Required | Description                                                      |
| :--------------- | :--- | :------- | :--------------------------------------------------------------- |
| media_partner_id | str  | ❌       | Your Impact partner ID as found on impact.com.                   |
| origin0          | str  | ❌       | IATA code or Entity ID for the origin of the first flight.       |
| date0            | str  | ❌       | Outbound date of the first flight in the format YYYY-MM-DD.      |
| destination0     | str  | ❌       | IATA code or Entity ID for the destination of the first flight.  |
| origin1          | str  | ❌       | IATA code or Entity ID for the origin of the second flight.      |
| date1            | str  | ❌       | Outbound date of the second flight in the format YYYY-MM-DD.     |
| destination1     | str  | ❌       | IATA code or Entity ID for the destination of the second flight. |
| origin2          | str  | ❌       | IATA code or Entity ID for the origin of the third flight.       |
| date2            | str  | ❌       | Outbound date of the third flight in the format YYYY-MM-DD.      |
| destination2     | str  | ❌       | IATA code or Entity ID for the destination of the third flight.  |
| adultsv2         | str  | ❌       | Number of adults.                                                |
| cabinclass       | str  | ❌       | The cabin class. Default is economy.                             |

**Example Usage Code Snippet**

```python
from skyscanner_referrals import SkyscannerReferrals, Environment

sdk = SkyscannerReferrals(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.flights.multi_city(
    media_partner_id="{{mediaPartnerId}}",
    origin0="CDG",
    date0="{{date0}}",
    destination0="EDI",
    origin1="EDI",
    date1="{{date1}}",
    destination1="BCN",
    origin2="BCN",
    date2="{{date2}}",
    destination2="AMS",
    adultsv2="4",
    cabinclass="business"
)

print(result)
```

## browse_view

Browse View

- HTTP Method: `GET`
- Endpoint: `/g/referrals/v1/flights/browse-view/`

**Parameters**

| Name             | Type | Required | Description                                         |
| :--------------- | :--- | :------- | :-------------------------------------------------- |
| media_partner_id | str  | ❌       | Your Impact partner ID as found on impact.com.      |
| origin           | str  | ❌       | Country code for the origin.                        |
| oym              | str  | ❌       | Departure date in YYYY-MM format.                   |
| iym              | str  | ❌       | Arrival date in YYYY-MM format.                     |
| rtn              | str  | ❌       | Type of the trip, e.g. oneway, return or multicity. |

**Example Usage Code Snippet**

```python
from skyscanner_referrals import SkyscannerReferrals, Environment

sdk = SkyscannerReferrals(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.flights.browse_view(
    media_partner_id="{{mediaPartnerId}}",
    origin="UK",
    oym="{{oym}}",
    iym="{{iym}}",
    rtn="oneway"
)

print(result)
```

## cheap_flights_to

Cheap Flights To

- HTTP Method: `GET`
- Endpoint: `/g/referrals/v1/flights/cheap-flights-to/`

**Parameters**

| Name             | Type | Required | Description                                    |
| :--------------- | :--- | :------- | :--------------------------------------------- |
| media_partner_id | str  | ❌       | Your Impact partner ID as found on impact.com. |
| destination      | str  | ❌       | IATA code or Entity ID for the destination.    |

**Example Usage Code Snippet**

```python
from skyscanner_referrals import SkyscannerReferrals, Environment

sdk = SkyscannerReferrals(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.flights.cheap_flights_to(
    media_partner_id="{{mediaPartnerId}}",
    destination="BCN"
)

print(result)
```

## flights_airline

Flights Airline

- HTTP Method: `GET`
- Endpoint: `/g/referrals/v1/flights/flights-airline/`

**Parameters**

| Name             | Type | Required | Description                                    |
| :--------------- | :--- | :------- | :--------------------------------------------- |
| media_partner_id | str  | ❌       | Your Impact partner ID as found on impact.com. |
| airline_code     | str  | ❌       | The airline code.                              |
| airline_name     | str  | ❌       | The airline name.                              |

**Example Usage Code Snippet**

```python
from skyscanner_referrals import SkyscannerReferrals, Environment

sdk = SkyscannerReferrals(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.flights.flights_airline(
    media_partner_id="{{mediaPartnerId}}",
    airline_code="DL",
    airline_name="Delta"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
