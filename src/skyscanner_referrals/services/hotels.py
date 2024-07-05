# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models


class HotelsService(BaseService):

    @cast_models
    def hotels_home(self, media_partner_id: str = None):
        """Hotels Home

        :param media_partner_id: Your Impact partner ID as found at Impact.com., defaults to None
        :type media_partner_id: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).is_optional().validate(media_partner_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/g/referrals/v1/hotels/home-view/",
                self.get_default_headers(),
            )
            .add_query("mediaPartnerId", media_partner_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def hotels_day_view(
        self,
        media_partner_id: str = None,
        entity_id: str = None,
        checkin: str = None,
        checkout: str = None,
        adults: str = None,
        rooms: str = None,
        utm_term: str = None,
    ):
        """Hotels Day View

        :param media_partner_id: Your Impact partner ID as found on impact.com., defaults to None
        :type media_partner_id: str, optional
        :param entity_id: Entity ID for the hotel/city., defaults to None
        :type entity_id: str, optional
        :param checkin: Check-in date in the format YYYY-MM-DD., defaults to None
        :type checkin: str, optional
        :param checkout: Check-out date in the format YYYY-MM-DD., defaults to None
        :type checkout: str, optional
        :param adults: Number of adults. Default is 2., defaults to None
        :type adults: str, optional
        :param rooms: Number of rooms. Default is 1., defaults to None
        :type rooms: str, optional
        :param utm_term: Additional alphanumeric tracking parameter you can add to your text links for additional tracking. This will be reported on Impact as Sub Id 2., defaults to None
        :type utm_term: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).is_optional().validate(media_partner_id)
        Validator(str).is_optional().validate(entity_id)
        Validator(str).is_optional().validate(checkin)
        Validator(str).is_optional().validate(checkout)
        Validator(str).is_optional().validate(adults)
        Validator(str).is_optional().validate(rooms)
        Validator(str).is_optional().validate(utm_term)

        serialized_request = (
            Serializer(
                f"{self.base_url}/g/referrals/v1/hotels/day-view",
                self.get_default_headers(),
            )
            .add_query("mediaPartnerId", media_partner_id)
            .add_query("entity_id", entity_id)
            .add_query("checkin", checkin)
            .add_query("checkout", checkout)
            .add_query("adults", adults)
            .add_query("rooms", rooms)
            .add_query("utm_term", utm_term)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def hotel_details(
        self,
        media_partner_id: str = None,
        hotel_id: str = None,
        checkin: str = None,
        checkout: str = None,
        adults: str = None,
        rooms: str = None,
    ):
        """Hotel Details

        :param media_partner_id: Your Impact partner ID as found on impact.com., defaults to None
        :type media_partner_id: str, optional
        :param hotel_id: Entity ID for the hotel., defaults to None
        :type hotel_id: str, optional
        :param checkin: Check-in date in the format YYYY-MM-DD., defaults to None
        :type checkin: str, optional
        :param checkout: Check-out date in the format YYYY-MM-DD., defaults to None
        :type checkout: str, optional
        :param adults: Number of adults. Default is 2., defaults to None
        :type adults: str, optional
        :param rooms: Number of rooms. Default is 1., defaults to None
        :type rooms: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).is_optional().validate(media_partner_id)
        Validator(str).is_optional().validate(hotel_id)
        Validator(str).is_optional().validate(checkin)
        Validator(str).is_optional().validate(checkout)
        Validator(str).is_optional().validate(adults)
        Validator(str).is_optional().validate(rooms)

        serialized_request = (
            Serializer(
                f"{self.base_url}/g/referrals/v1/hotels/hotel-details",
                self.get_default_headers(),
            )
            .add_query("mediaPartnerId", media_partner_id)
            .add_query("hotelId", hotel_id)
            .add_query("checkin", checkin)
            .add_query("checkout", checkout)
            .add_query("adults", adults)
            .add_query("rooms", rooms)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return response
