# revenue_engine.py
# Motori i të ardhurave që përpunon informacionet nga market_scanner

from market_scanner import scan_market

def process_opportunities():
    """
    Proceson mundësitë e gjetura nga market_scanner dhe i shndërron në të ardhura potenciale.
    """
    info = scan_market()
    return f"Revenue Engine aktiv. Po përpunon: {info}"

if __name__ == "__main__":
    print(process_opportunities())
