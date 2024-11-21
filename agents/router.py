from agents.data_agent import handle_product_query
from agents.general_qa import handle_general_query

def route_query(query: str) -> str:
    product_keywords = ["product", "price", "details", "buy", "specification", "features", 
                       "cost", "availability", "brand", "compare", "review", "delivery"]
    
    if any(keyword in query.lower() for keyword in product_keywords):
        return handle_product_query(query)
    else:
        return handle_general_query(query)