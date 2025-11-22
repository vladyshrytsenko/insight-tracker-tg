from typing import Dict, Any, List
import logging

logger = logging.getLogger(__name__)

class GamblingKPICalculator:
    @staticmethod
    def normalize_stats(raw_stats: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize raw Facebook insights into gambling KPIs."""
        if not raw_stats:
            return {}

        # Basic metrics
        spend = float(raw_stats.get("spend", 0))
        impressions = int(raw_stats.get("impressions", 0))
        clicks = int(raw_stats.get("clicks", 0))
        ctr = float(raw_stats.get("ctr", 0).strip('%')) / 100 if raw_stats.get("ctr") else 0
        cpc = float(raw_stats.get("cpc", 0))
        cpm = float(raw_stats.get("cpm", 0))

        # Parse actions
        actions = raw_stats.get("actions", [])
        action_dict = {action["action_type"]: int(action["value"]) for action in actions}

        installs = action_dict.get("mobile_app_install", 0)
        registrations = action_dict.get("registration_completed", 0)
        deposits = action_dict.get("purchase", 0)  # Assuming purchase is deposit

        # Revenue from action_values
        action_values = raw_stats.get("action_values", [])
        revenue = 0.0
        for av in action_values:
            if av["action_type"] == "purchase":
                revenue = float(av["value"])
                break

        # Cost per action
        cost_per_action = raw_stats.get("cost_per_action_type", [])
        cpa_dict = {cpa["action_type"]: float(cpa["value"]) for cpa in cost_per_action}

        cpi = cpa_dict.get("mobile_app_install", 0)
        cpr = cpa_dict.get("registration_completed", 0)
        cpd = cpa_dict.get("purchase", 0)

        # ROAS
        roas = revenue / spend if spend > 0 else 0

        # Conversion rates
        cr_click_install = (installs / clicks) * 100 if clicks > 0 else 0
        cr_install_reg = (registrations / installs) * 100 if installs > 0 else 0
        cr_reg_dep = (deposits / registrations) * 100 if registrations > 0 else 0

        # Rankings
        quality_ranking = raw_stats.get("quality_ranking", "UNKNOWN")
        conversion_rate_ranking = raw_stats.get("conversion_rate_ranking", "UNKNOWN")
        engagement_rate_ranking = raw_stats.get("engagement_rate_ranking", "UNKNOWN")

        return {
            "spend": spend,
            "impressions": impressions,
            "clicks": clicks,
            "ctr": ctr,
            "cpc": cpc,
            "cpm": cpm,
            "installs": installs,
            "registrations": registrations,
            "deposits": deposits,
            "revenue": revenue,
            "roas": roas,
            "cpi": cpi,
            "cpr": cpr,
            "cpd": cpd,
            "cr_click_install": cr_click_install,
            "cr_install_reg": cr_install_reg,
            "cr_reg_dep": cr_reg_dep,
            "quality_ranking": quality_ranking,
            "conversion_rate_ranking": conversion_rate_ranking,
            "engagement_rate_ranking": engagement_rate_ranking,
        }