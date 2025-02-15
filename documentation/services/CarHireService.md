# CarHireService

A list of all methods in the `CarHireService` service. Click on the method name to view detailed information about that method.

| Methods                                 | Description       |
| :-------------------------------------- | :---------------- |
| [car_home](#car_home)                   | Car Home          |
| [car_hire_day_view](#car_hire_day_view) | Car Hire Day View |

## car_home

Car Home

- HTTP Method: `GET`
- Endpoint: `/g/referrals/v1/cars/home/`

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

result = sdk.car_hire.car_home(media_partner_id="{{mediaPartnerId}}")

print(result)
```

## car_hire_day_view

Car Hire Day View

- HTTP Method: `GET`
- Endpoint: `/g/referrals/v1/cars/day-view/`

**Parameters**

| Name             | Type | Required | Description                                                                                                                                     |
| :--------------- | :--- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| media_partner_id | str  | ❌       | Your Impact partner ID as found at Impact.com.                                                                                                  |
| pickup_place     | str  | ❌       | IATA code or Entity ID for the pick-up place.                                                                                                   |
| dropoff_place    | str  | ❌       | IATA code or Entity ID for the drop-off place.                                                                                                  |
| pickup_time      | str  | ❌       | Pick-up datetime in ISO 8601 standard. e.g. YYYY-MM-DDTHH:MM.                                                                                   |
| dropoff_time     | str  | ❌       | Drop-off datetime in ISO 8601 standard. e.g. YYYY-MM-DDTHH:MM.                                                                                  |
| driver_age       | str  | ❌       | Driver age between 21 and 99. Default age is 30.                                                                                                |
| utm_term         | str  | ❌       | Additional alphanumeric tracking parameter you can add to your text links for additional tracking. This will be reported on Impact as Sub Id 2. |

**Example Usage Code Snippet**

```python
from skyscanner_referrals import SkyscannerReferrals, Environment

sdk = SkyscannerReferrals(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.car_hire.car_hire_day_view(
    media_partner_id="{{mediaPartnerId}}",
    pickup_place="BCN",
    dropoff_place="AMS",
    pickup_time="{{pickupTime}}",
    dropoff_time="{{dropoffTime}}",
    driver_age="35",
    utm_term="summer"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
