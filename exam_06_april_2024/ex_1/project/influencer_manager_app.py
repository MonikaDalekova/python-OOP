from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    INFLUENCER_TYPES = {
        "PremiumInfluencer": PremiumInfluencer,
        "StandardInfluencer": StandardInfluencer
    }
    CAMPAIGN_TYPES = {
        "HighBudgetCampaign": HighBudgetCampaign,
        "LowBudgetCampaign": LowBudgetCampaign
    }

    def __init__(self):
        self.influencers = [] #influencer objects registered with the Influencer Manager
        self.campaigns = [] #all campaign objects that are scheduled to start

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.INFLUENCER_TYPES.keys():
            return f"{influencer_type} is not an allowed influencer type."
        influencer = next((i for i in self.influencers if i.username == username), None)
        if influencer:
            return f"{username} is already registered."
        new_influencer = self.INFLUENCER_TYPES[influencer_type](username, followers, engagement_rate)
        self.influencers.append(new_influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.CAMPAIGN_TYPES.keys():
            return f"{campaign_type} is not a valid campaign type."
        camp = next((c for c in self.campaigns if c.campaign_id == campaign_id), None)
        if camp:
            return f"Campaign ID {campaign_id} has already been created."
        new_campaign = self.CAMPAIGN_TYPES[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(new_campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = next((i for i in self.influencers if i.username == influencer_username), None)
        camp = next((c for c in self.campaigns if c.campaign_id == campaign_id), None)

        if not influencer:
            return f"Influencer '{influencer_username}' not found."
        if not camp:
            return f"Campaign with ID {campaign_id} not found."
        if not camp.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility " \
                   f"criteria for the campaign with ID {campaign_id}."
        payment = influencer.calculate_payment(camp)
        if payment > 0.0:
            camp.approved_influencers.append(influencer)
            #TODO to check with cap letters
            camp.budget -= payment
            influencer.campaigns_participated.append(camp)
            return f"Influencer '{influencer_username}' has successfully " \
                   f"participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        total_reached_followers = {}
        for influencer in self.influencers:
            for camp in influencer.campaigns_participated:
                reached_followers = influencer.reached_followers(type(camp).__name__)
                total_reached_followers[camp] = total_reached_followers.get(camp, 0) + reached_followers
        return total_reached_followers

    def influencer_campaign_report(self, username: str):
        influencer = next((i for i in self.influencers if i.username == username), None)
        if influencer:
            return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        total_reached_followers = self.calculate_total_reached_followers()

        sorted_campaigns = sorted(self.campaigns, key=lambda x: (len(x.approved_influencers), -x.budget))

        campaign_stats = [
            f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, "
            f"Total budget: ${campaign.budget:.2f}, Total reached followers: {total_reached_followers.get(campaign, 0)}"
            for campaign in sorted_campaigns
        ]

        return f"$$ Campaign Statistics $$\n" + "\n".join(campaign_stats)
