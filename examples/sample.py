# This file was generated by liblab | https://liblab.com/

from skyscanner_referrals import SkyscannerReferrals, Environment

sdk = SkyscannerReferrals(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
)

result = sdk.flights.flights_home(media_partner_id="{{mediaPartnerId}}")

print(result)
