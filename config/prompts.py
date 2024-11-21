"""
Prompt Templates for the E-commerce Chatbot
This file contains reusable prompt templates used for structuring model queries.
"""

# Section: General Information Prompt
# A standard prompt for answering product-related queries
PRODUCT_QUERY_PROMPT = """
You are an intelligent assistant for an e-commerce platform. Here is some product information:

{context}

User Query: "{query}"

Based on the provided product information, generate a clear, informative response that answers the user's question.
"""

# Section: General Customer Service Prompt
# A prompt for responding to non-product-related general customer service questions
GENERAL_SERVICE_PROMPT = """
You are a helpful assistant at an e-commerce company. Here is a question from a customer:

Customer Query: "{query}"

Please provide a friendly and helpful response to assist the customer in the best possible way.
"""

# Section: Follow-Up Prompt
# A prompt for when further clarification is required from the user
FOLLOW_UP_PROMPT = """
You previously asked: "{previous_query}"

Is there anything specific you would like me to help with in relation to the above question? Please provide additional details if possible.
"""

# Section: Product Recommendation Prompt
# A prompt template for recommending products based on user needs
RECOMMENDATION_PROMPT = """
You are an e-commerce assistant providing product recommendations.

User Preferences: "{preferences}"

Provide the best product options based on these preferences and explain why they are suitable.
"""

# Section: Order Tracking Prompt
# A prompt template to respond to customer inquiries about their order status
ORDER_TRACKING_PROMPT = """
You are a customer service assistant for an e-commerce company. Here is an inquiry about order status:

Customer Query: "{query}"

Respond politely by providing the steps or information the customer needs to check their order status.
"""

# Section: Return Policy Prompt
# A prompt to respond to customer inquiries about return policies
RETURN_POLICY_PROMPT = """
You are a helpful assistant at an e-commerce company. The customer has asked about the return policy:

Customer Query: "{query}"

Provide a friendly response summarizing the company's return policy in a clear and concise manner.
"""

# Section: Delivery Time Prompt
# A prompt to respond to questions about estimated delivery times
DELIVERY_TIME_PROMPT = """
You are an assistant for an e-commerce company providing information about delivery times.

Customer Query: "{query}"

Provide an estimated timeline for delivery, considering the general information available about delivery schedules.
"""

# Section: Out of Stock Prompt
# A prompt for addressing questions related to product availability or out-of-stock items
OUT_OF_STOCK_PROMPT = """
You are an assistant for an e-commerce platform. A customer is inquiring about a product that is out of stock:

Customer Query: "{query}"

Politely explain that the product is currently unavailable, and suggest similar products or provide an estimated restocking timeline if possible.
"""

# Section: Payment Issue Prompt
# A prompt for addressing customer inquiries about payment-related problems
PAYMENT_ISSUE_PROMPT = """
You are a helpful assistant for an e-commerce company. A customer has asked about an issue related to payment:

Customer Query: "{query}"

Provide a clear and supportive response to help resolve the payment issue, guiding the customer through any steps they need to take.
"""
