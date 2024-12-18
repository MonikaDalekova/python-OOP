from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    INFLUENCER_TYPE = "Standart"
    INITIAL_PAYMENT_PERCENTAGE = 0.45

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign: BaseCampaign):
        return campaign.budget * self.INITIAL_PAYMENT_PERCENTAGE

    def reached_followers(self, campaign_type: str):
        reached_followers = 0
        if campaign_type == "HighBudgetCampaign":
            reached_followers = self.followers * self.engagement_rate * 1.2
        elif campaign_type == "LowBudgetCampaign":
            reached_followers = self.followers * self.engagement_rate * 0.9
        return reached_followers
