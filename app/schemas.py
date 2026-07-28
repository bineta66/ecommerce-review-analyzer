from pydantic import BaseModel, Field



class ReviewRequest(BaseModel):

    text: str = Field(

        ...,

        min_length=5,

        description="Avis client"

    )




class ReviewResponse(BaseModel):

    sentiment: str

    sentiment_confidence: float

    is_urgent: bool

    urgency_category: str

    urgency_confidence: float