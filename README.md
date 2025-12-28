# Neutrals-Smart-Pricing

Neutrals-Smart-Pricing is an AI-driven smart dynamic pricing system inspired by quick-commerce platforms like Blinkit.
The system intelligently predicts optimized product prices by analyzing demand, supply, competitor prices, and product expiry, ensuring fair pricing for both customers and sellers.

This project also includes image-based product search, allowing users to search products simply by uploading an image.

## 1. What Problem Does It Solve?

  1. Static pricing fails in fast-moving e-commerce environments

  2. Perishable goods need expiry-aware pricing

  3. Customers want competitive and fair prices

  4. Searching products using text is slow and inconvenient

  Neutrals-Smart-Pricing solves these using AI + Machine Learning.

## 2. Key Features
  ### 1. Smart Dynamic Pricing (ML-Based)

  Predicts optimized product price dynamically

  Considers:

  Base Price

  Competitor Price

  Demand level

  Supply level

  Expiry days

  ### 2. Demand & Supply Intelligence

  Products are classified as:

  Low (0)

  Medium (1)

  High (2)

  Helps identify:

  Most demanded products

  Overstocked products

  Balanced inventory items

  ### 3. Image-Based Product Search (AI)

  User uploads a product image

  AI matches image with product catalog

  Displays best matching product card

  No manual typing required

  ### 4. Firebase Integration

  Real-time product data storage

  Stores:

  Product details

  Demand & supply values

  Optimized price

  Updates optimized price back to database

  ### 5. Real-Time Price Optimization

  Prices automatically adjust when:

  Demand changes

  Supply changes

  Expiry date approaches

  Optimized price stored with 2-decimal precision

## 6. Machine Learning Approach
  ### 1. Model Used

  XGBoost Regressor

  ### 2. Input Features

  1. Base Price

  2. Competitor Price

  3. Demand (0/1/2)

  4. Supply (0/1/2)

  5. Expiry Days

  ### 3. Output

  Optimized Price

  The model learns real-world pricing behavior and avoids large price jumps, keeping prices realistic and market-friendly.

##  7. Image Search Intelligence

  Uses CLIP (Contrastive Language-Image Pretraining)

  Converts:

  Product images → embeddings

  Product names → embeddings

  Finds the best match using cosine similarity

  Enables visual product search

##   8. Use Cases

  1. Quick-commerce platforms

  2. Grocery delivery apps

  3. Inventory-heavy businesses

  4. Perishable goods pricing

  5. AI-based retail analytics


