#!/usr/bin/env python3
"""Generate Leboncoin Real Estate & Vehicles product roadmap PDF (English)."""

from pathlib import Path

from fpdf import FPDF


class RoadmapPDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, "Leboncoin Platform Roadmap | Real Estate & Vehicles", align="R")
        self.ln(12)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def cover_block(self):
        self.set_font("Helvetica", "B", 28)
        self.set_text_color(30, 30, 30)
        self.ln(25)
        self.multi_cell(0, 14, "Leboncoin.fr", align="C")
        self.ln(4)
        self.set_font("Helvetica", "", 16)
        self.set_text_color(60, 60, 60)
        self.multi_cell(0, 10, "Product & Service Roadmap", align="C")
        self.ln(6)
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(0, 102, 153)
        self.multi_cell(0, 8, "Real Estate  |  Vehicles", align="C")
        self.ln(20)
        self.set_font("Helvetica", "", 11)
        self.set_text_color(80, 80, 80)
        self.multi_cell(
            0,
            7,
            "Strategic overview for France's leading classifieds marketplace.\n"
            "Focus: two verticals only - Immobilier (Real Estate) and Vehicules (Vehicles).",
            align="C",
        )
        self.ln(30)
        self.set_font("Helvetica", "I", 10)
        self.cell(0, 6, "Document language: English", align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 6, "Version 1.0 | June 2026", align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 6, "Prepared for export and stakeholder review", align="C")

    def section_title(self, title: str, level: int = 1):
        self.ln(6 if level == 1 else 4)
        size = 16 if level == 1 else 13
        self.set_font("Helvetica", "B", size)
        self.set_text_color(0, 102, 153 if level == 1 else 51)
        self.multi_cell(0, 8, title)
        self.set_draw_color(0, 102, 153)
        self.set_line_width(0.4)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(4)

    def subsection(self, title: str):
        self.ln(3)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 7, title)
        self.ln(1)

    def body_text(self, text: str):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def bullet(self, text: str, indent: int = 0):
        self.ensure_space(12)
        x = self.l_margin + indent
        self.set_x(x)
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        width = self.w - self.r_margin - x
        self.multi_cell(width, 5.5, f"- {text}")

    def ensure_space(self, height: float):
        if self.get_y() + height > self.h - self.b_margin:
            self.add_page()

    def phase_block(self, phase: str, timeline: str, deliverables: str):
        self.ensure_space(28)
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(0, 102, 153)
        self.multi_cell(0, 6, f"{phase} ({timeline})")
        self.set_x(self.l_margin)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5.5, deliverables)
        self.ln(3)


def build_pdf(output_path: Path) -> None:
    pdf = RoadmapPDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()
    pdf.cover_block()

    pdf.add_page()
    pdf.section_title("1. Executive Summary")
    pdf.body_text(
        "Leboncoin (www.leboncoin.fr) is France's largest general classifieds platform, "
        "owned by Adevinta. Among dozens of categories, Real Estate (Immobilier) and "
        "Vehicles (Vehicules) are two of the highest-value verticals: high transaction "
        "values, strong professional (B2B) participation, and recurring user journeys "
        "(search, compare, contact, visit, negotiate, close)."
    )
    pdf.body_text(
        "This roadmap describes the current platform capabilities, near-term priorities, "
        "and medium-to-long-term evolution for these two services only. It is based on "
        "public product announcements, industry positioning, and typical marketplace "
        "patterns - intended for planning, education, and export; not an official "
        "Leboncoin internal document."
    )

    pdf.section_title("2. Platform Context (France)")
    pdf.subsection("2.1 User segments")
    pdf.bullet("Private sellers and buyers (particuliers)")
    pdf.bullet("Professional agents, dealerships, and property managers (professionnels)")
    pdf.bullet("Renters and landlords in real estate sub-categories")
    pdf.subsection("2.2 Shared platform foundations")
    pdf.bullet("Account, messaging, favorites, alerts, and mobile apps (iOS/Android)")
    pdf.bullet("Search with filters, map view, and geo-localization across France")
    pdf.bullet("Paid listing options and visibility boosts (e.g. bump, highlight)")
    pdf.bullet("Trust & safety: reporting, moderation, secure payment flows where enabled")
    pdf.bullet("AI-assisted ad creation and visual search (rolling out by category)")

    pdf.section_title("3. Real Estate Service Roadmap")
    pdf.body_text(
        "Real Estate on Leboncoin covers sales, rentals, flat-sharing (colocation), "
        "new builds, land, and commercial property. Professionals use dedicated tools "
        "(Leboncoin Immo Pro); individuals face listing limits and fees on repeat ads."
    )

    pdf.subsection("3.1 Current state (baseline)")
    pdf.bullet("Listing creation with photos, price, surface (m2), rooms, location, DPE")
    pdf.bullet("Advanced filters: budget, property type, furnished, energy class, etc.")
    pdf.bullet("Map-based search and saved search alerts")
    pdf.bullet("In-app messaging between prospects and advertisers")
    pdf.bullet("Virtual video tours on professional listings")
    pdf.bullet("DPE labels on result cards (from class D onward, color-coded)")
    pdf.bullet("Highlights on results: balcony, terrace, pool, etc.")
    pdf.bullet("La bonne estimation - AI pricing tool for pros with downloadable reports")
    pdf.bullet("Lead qualification: richer contact forms with prospect criteria")
    pdf.bullet("Call tracking for professionals (missed-call follow-up)")
    pdf.bullet("Cercle de l'immo - professional feedback panel and sector insights")

    pdf.subsection("3.2 Real Estate - phased roadmap")
    for phase, timeline, desc in [
        (
            "Phase 1",
            "Now - 6 months",
            "Stabilize DPE display, result highlights, estimation reports; "
            "expand customizable contact forms for pros.",
        ),
        (
            "Phase 2",
            "6 - 18 months",
            "AI-generated property descriptions (domain-tuned); "
            "neighborhood POI and commute hints in listings; "
            "deeper colocation and student rental flows.",
        ),
        (
            "Phase 3",
            "18 - 36 months",
            "End-to-end rental journey (application, documents, deposit escrow where legal); "
            "3D and immersive tours at scale; integration with notaires and agents APIs.",
        ),
        (
            "Phase 4",
            "36+ months",
            "Predictive market analytics for pros; sustainability scoring; "
            "cross-listing syndication standards; optional transaction marketplace layer.",
        ),
    ]:
        pdf.phase_block(phase, timeline, desc)

    pdf.ln(4)
    pdf.subsection("3.3 Real Estate - key metrics to track")
    pdf.bullet("Qualified leads per listing and time-to-first-response")
    pdf.bullet("Estimation tool adoption and report downloads (pro segment)")
    pdf.bullet("Search-to-contact and contact-to-visit conversion")
    pdf.bullet("Listing quality score (photos, completeness, DPE accuracy)")
    pdf.bullet("Professional retention and ARPU vs. SeLoger, Bien'ici, etc.")

    pdf.add_page()
    pdf.section_title("4. Vehicles Service Roadmap")
    pdf.body_text(
        "The Vehicles vertical covers cars, motorcycles, utility vehicles, caravans, "
        "and parts. It competes with AutoScout24, La Centrale, and dealer sites. "
        "Leboncoin has pioneered AI ad copy and visual search in mobility categories."
    )

    pdf.subsection("4.1 Current state (baseline)")
    pdf.bullet("Detailed vehicle attributes: make, model, year, mileage, fuel, gearbox")
    pdf.bullet("Filters for price, location, seller type (private vs. pro)")
    pdf.bullet("Photo galleries and optional history / maintenance hints in description")
    pdf.bullet("AI-assisted ad description from photos + basic fields")
    pdf.bullet("Visual search: upload a photo to find similar listings (consumer + vehicles)")
    pdf.bullet("Messaging and phone contact; dealer storefronts for professionals")
    pdf.bullet("Paid visibility and listing fees for repeat private ads (policy updates)")

    pdf.subsection("4.2 Vehicles - phased roadmap")
    for phase, timeline, desc in [
        (
            "Phase 1",
            "Now - 6 months",
            "Widen AI description coverage; improve VIN/plate-assisted pre-fill where allowed; "
            "standardize pro inventory bulk upload.",
        ),
        (
            "Phase 2",
            "6 - 18 months",
            "Integrated history checks (accident, mileage fraud signals via partners); "
            "financing and insurance quote widgets; test-drive scheduling.",
        ),
        (
            "Phase 3",
            "18 - 36 months",
            "Secure deposit / reservation payments; remote video inspection; "
            "electric vehicle-specific filters (battery health, range).",
        ),
        (
            "Phase 4",
            "36+ months",
            "Full purchase workflow partnerships (registration, delivery); "
            "C2B trade-in quoting; fleet tools for dealers.",
        ),
    ]:
        pdf.phase_block(phase, timeline, desc)

    pdf.ln(4)
    pdf.subsection("4.3 Vehicles - key metrics to track")
    pdf.bullet("Listing completeness and AI description acceptance rate")
    pdf.bullet("Visual search usage and conversion to contact")
    pdf.bullet("Average days-on-market by segment (private vs. pro)")
    pdf.bullet("Dealer inventory sync freshness and lead quality")
    pdf.bullet("Share of listings with verified history or warranty badges")

    pdf.section_title("5. Cross-Cutting Initiatives (Both Verticals)")
    pdf.bullet("Trust: identity verification, scam detection, review signals where applicable")
    pdf.bullet("Payments: Leboncoin Pay / escrow patterns for high-trust transactions")
    pdf.bullet("AI: category-specific models, human-in-the-loop moderation of generated copy")
    pdf.bullet("Regulation: DPE, consumer law, automotive advertising rules in France")
    pdf.bullet("Sustainability: EV/green labels (vehicles), energy performance (real estate)")
    pdf.bullet("Mobile-first UX, performance, and accessibility (WCAG)")

    pdf.section_title("6. User Journey Maps (Simplified)")
    pdf.subsection("6.1 Real Estate - buyer journey")
    pdf.bullet("Discover (search/alerts/map) -> Evaluate (filters, DPE, highlights, media)")
    pdf.bullet("Contact (form with criteria / message / call) -> Visit -> Negotiate -> Close")
    pdf.subsection("6.2 Vehicles - buyer journey")
    pdf.bullet("Discover (search/visual AI) -> Compare (specs, price, history) -> Contact")
    pdf.bullet("Inspect (in person or video) -> Finance (optional) -> Purchase")

    pdf.section_title("7. Risks & Dependencies")
    pdf.bullet("Competitive pressure from specialized portals (SeLoger, La Centrale, etc.)")
    pdf.bullet("Regulatory changes (rent controls, DPE rules, automotive emissions labels)")
    pdf.bullet("Data partnerships for history, estimation, and POI content")
    pdf.bullet("Balancing monetization (listing fees) with private seller liquidity")
    pdf.bullet("Legal constraints on scraping and third-party aggregators")

    pdf.section_title("8. Appendix")
    pdf.subsection("8.1 Official resources")
    pdf.bullet("Main site: https://www.leboncoin.fr/")
    pdf.bullet("Real estate: https://www.leboncoin.fr/c/ventes_immobilieres")
    pdf.bullet("Vehicles: https://www.leboncoin.fr/c/voitures")
    pdf.bullet("Pro solutions: https://leboncoinsolutionspro.fr/")
    pdf.subsection("8.2 Document disclaimer")
    pdf.body_text(
        "This roadmap is an independent English-language summary for educational and "
        "planning purposes. Feature names, timelines, and priorities may differ from "
        "actual Leboncoin product plans. Always refer to official Leboncoin communications "
        "for contractual or investment decisions."
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(output_path))


if __name__ == "__main__":
    out = Path(__file__).resolve().parents[1] / "docs" / "Leboncoin_Roadmap_RealEstate_Vehicles_EN.pdf"
    build_pdf(out)
    print(f"Generated: {out}")
