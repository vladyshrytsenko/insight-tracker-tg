from typing import Dict, Any

class TelegramFormatter:
    @staticmethod
    def format_today_performance(stats: Dict[str, Any], analysis: str) -> str:
        """Format today's performance data into Telegram message."""
        if not stats:
            return "📊 No data available for today."

        message = "📊 TODAY'S GAMBLING PERFORMANCE\n\n"
        message += f"Spend: ${stats['spend']:.2f}\n"
        message += f"Installs: {stats['installs']} (CPI ${stats['cpi']:.2f})\n"
        message += f"Regs: {stats['registrations']} (CPR ${stats['cpr']:.2f})\n"
        message += f"Deps: {stats['deposits']} (CPD ${stats['cpd']:.2f})\n"
        message += f"Revenue: ${stats['revenue']:.2f}\n"
        message += f"ROAS: {stats['roas']:.2f}\n\n"

        message += "Funnel:\n"
        message += f"Click → Install: {stats['cr_click_install']:.1f}%\n"
        message += f"Install → Reg: {stats['cr_install_reg']:.1f}%\n"
        message += f"Reg → Dep: {stats['cr_reg_dep']:.1f}%\n\n"

        message += f"⚠️ AI Analysis:\n{analysis}"

        return message