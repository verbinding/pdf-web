from pydantic import BaseModel

class PersonIdentifyRequest(BaseModel):
    name: str = None
    first_name: str = None
    last_name: str = None
    middle_name: str = None
    location: str = None
    street_address: str = None
    locality: str = None
    region: str = None
    country: str = None
    postal_code: str = None
    company: str = None
    school: str = None
    phone: str = None
    email: str = None
    email_hash: str = None
    profile: str = None
    linkedin: str = None
    birth_date: str = None
