Neutrals-Smart-Pricing

Neutrals-Smart-Pricing is an AI-driven smart dynamic pricing system inspired by quick-commerce platforms like Blinkit.
The system intelligently predicts optimized product prices by analyzing demand, supply, competitor prices, and product expiry, ensuring fair pricing for both customers and sellers.

This project also includes image-based product search, allowing users to search products simply by uploading an image.

🚀 What Problem Does It Solve?

Static pricing fails in fast-moving e-commerce environments

Perishable goods need expiry-aware pricing

Customers want competitive and fair prices

Searching products using text is slow and inconvenient

Neutrals-Smart-Pricing solves these using AI + Machine Learning.

✨ Key Features
🔹 Smart Dynamic Pricing (ML-Based)

Predicts optimized product price dynamically

Considers:

Base Price

Competitor Price

Demand level

Supply level

Expiry days

🔹 Demand & Supply Intelligence

Products are classified as:

Low (0)

Medium (1)

High (2)

Helps identify:

Most demanded products

Overstocked products

Balanced inventory items

🔹 Image-Based Product Search (AI)

User uploads a product image

AI matches image with product catalog

Displays best matching product card

No manual typing required

🔹 Firebase Integration

Real-time product data storage

Stores:

Product details

Demand & supply values

Optimized price

Updates optimized price back to database

🔹 Real-Time Price Optimization

Prices automatically adjust when:

Demand changes

Supply changes

Expiry date approaches

Optimized price stored with 2-decimal precision

🧠 Machine Learning Approach
Model Used

XGBoost Regressor

Input Features

Base Price

Competitor Price

Demand (0/1/2)

Supply (0/1/2)

Expiry Days

Output

Optimized Price

The model learns real-world pricing behavior and avoids large price jumps, keeping prices realistic and market-friendly.

🖼️ Image Search Intelligence

Uses CLIP (Contrastive Language-Image Pretraining)

Converts:

Product images → embeddings

Product names → embeddings

Finds the best match using cosine similarity

Enables visual product search

📊 Use Cases

Quick-commerce platforms

Grocery delivery apps

Inventory-heavy businesses

Perishable goods pricing

AI-based retail analytics

🔮 Future Enhancements

Live competitor price scraping

Reinforcement learning for pricing

Customer behavior-based pricing

Admin analytics dashboard

Mobile application integration
