# Product Roadmap: France Classifieds Marketplace

## Scope

This roadmap describes a France-focused online classifieds marketplace inspired by the Leboncoin model, limited to two services:

1. Real Estate
2. Vehicles

The goal is to launch a trusted marketplace where private users and professional sellers can publish, search, compare, and manage listings.

## Product Vision

Build a simple, trusted, mobile-first marketplace for high-intent buyers, renters, sellers, and agents in France. The platform should make it easy to discover local real estate and vehicle offers, contact sellers safely, and manage listings with clear pricing and verification options.

## Target Users

### Real Estate

- Private landlords and property owners
- Real estate agencies
- Tenants looking for rentals
- Buyers looking for homes, apartments, land, or commercial property

### Vehicles

- Private vehicle sellers
- Professional car dealers
- Buyers looking for used or new cars, motorcycles, vans, and utility vehicles

## Core Marketplace Capabilities

### User Accounts

- Email, phone, and social login
- Buyer, private seller, and professional seller profiles
- Profile verification using phone and email
- Seller dashboard for listings, messages, payments, and performance

### Listing Management

- Create, edit, pause, renew, and delete listings
- Image upload with cropping and compression
- Listing preview before publication
- Draft listings
- Moderation status: pending, approved, rejected, expired
- Abuse reporting and seller blocking

### Search and Discovery

- Location-based search across France
- Map and list views
- Saved searches
- Favorites
- Filters by category-specific attributes
- Sorting by relevance, newest, price, location, and seller type

### Messaging and Leads

- Secure buyer-seller messaging
- Lead forms for professional sellers
- Phone reveal tracking
- Email notifications
- Optional in-app notifications

### Trust and Safety

- Phone and email verification
- Listing moderation
- Duplicate listing detection
- Scam and spam reporting
- Professional seller badges
- Clear safety tips on listing and messaging pages

## Service 1: Real Estate

### MVP Features

- Property categories: rent, buy, shared housing, land, commercial property
- Property type: apartment, house, studio, office, shop, parking, land
- Required fields: price, location, surface area, number of rooms, photos, description, seller type
- Optional fields: bedrooms, bathrooms, furnished, energy rating, heating type, floor, elevator, balcony, parking, availability date
- Search filters: price range, location radius, property type, surface area, rooms, seller type
- Map search and nearby listings
- Contact form and secure messaging

### Post-MVP Features

- Agency storefronts
- Property alerts
- Lead scoring for professional sellers
- Document checklist for rentals
- Virtual tour links
- Energy Performance Diagnosis fields
- Neighborhood insights
- Featured real estate listings

## Service 2: Vehicles

### MVP Features

- Vehicle categories: cars, motorcycles, vans, utility vehicles
- Required fields: price, make, model, year, mileage, fuel type, transmission, location, photos, description, seller type
- Optional fields: engine power, emissions, number of doors, color, service history, warranty, Crit'Air class
- Search filters: price range, location radius, make, model, year, mileage, fuel, transmission, seller type
- Vehicle listing detail page with key specifications
- Contact form and secure messaging

### Post-MVP Features

- Dealer storefronts
- Vehicle history report integration
- Financing lead forms
- Insurance partner offers
- Price valuation guidance
- Saved vehicle comparisons
- Featured vehicle listings

## Roadmap Phases

### Phase 1: Foundation and Marketplace Core

- Define product requirements and category data models
- Build responsive web application
- Implement user registration and login
- Build seller dashboard
- Implement listing creation, editing, expiration, and moderation workflow
- Add image upload and optimization
- Add secure messaging
- Prepare GDPR-compliant consent, privacy, and account deletion flows

### Phase 2: Real Estate MVP

- Launch real estate listing creation flow
- Add property-specific attributes and validations
- Build real estate search filters
- Add map-based discovery
- Add saved searches and favorites
- Build real estate listing detail pages
- Add professional agency profile support

### Phase 3: Vehicle MVP

- Launch vehicle listing creation flow
- Add vehicle-specific attributes and validations
- Build vehicle search filters
- Add vehicle detail pages with specification sections
- Add dealer profile support
- Add saved vehicle searches and favorites

### Phase 4: Trust, Safety, and Operations

- Add automated moderation rules
- Add manual admin review queue
- Add user reporting tools
- Add duplicate and suspicious listing detection
- Add phone verification for sellers
- Add audit logs for listing and moderation actions
- Add customer support workflows

### Phase 5: Monetization

- Paid listing boosts
- Featured listings on search result pages
- Professional seller subscriptions
- Agency and dealer storefront packages
- Lead packages for professionals
- Optional partner offers for financing, insurance, moving, and diagnostics

### Phase 6: Growth and Optimization

- SEO landing pages for cities, regions, property types, makes, and models
- Email alerts for saved searches
- Analytics dashboards for professional sellers
- A/B testing for listing forms and contact flows
- Mobile app or progressive web app enhancements
- Recommendation engine for similar listings

## Suggested MVP Information Architecture

- Home
- Real Estate
  - Buy
  - Rent
  - Shared Housing
  - Commercial Property
- Vehicles
  - Cars
  - Motorcycles
  - Vans and Utility Vehicles
- Search Results
- Listing Detail
- Post an Ad
- Messages
- Favorites
- Saved Searches
- Seller Dashboard
- Professional Seller Page
- Help and Safety Center

## Admin and Back Office

- User management
- Listing moderation
- Category and attribute management
- Reported content queue
- Payment and invoice management
- Professional seller management
- Support ticket tracking
- Analytics and fraud monitoring

## Technology and Platform Considerations

- Mobile-first responsive web experience
- Structured category schemas for real estate and vehicles
- Search engine with geolocation support
- Image storage and CDN delivery
- Event tracking for listing views, contacts, phone reveals, and favorites
- Role-based access control for users, professionals, moderators, and admins
- GDPR-compliant data handling, consent, deletion, and export
- Scalable architecture for high listing volume and search traffic

## Compliance Notes for France

- GDPR privacy policy, cookie consent, data export, and account deletion
- Clear professional seller identification
- Real estate energy performance fields where applicable
- Transparent paid promotion labeling
- Secure handling of user communications
- Terms of use, prohibited listings, and moderation policy

## Key Success Metrics

### Marketplace Metrics

- Number of active listings
- Number of verified sellers
- Search-to-contact conversion rate
- Listing approval time
- Reported listing rate
- Repeat seller rate

### Real Estate Metrics

- Real estate listing volume by city and region
- Rental and sale lead conversion rate
- Saved searches per user
- Agency subscription conversion

### Vehicle Metrics

- Vehicle listing volume by make and model
- Dealer subscription conversion
- Contact rate per vehicle listing
- Average listing age before removal

## Recommended MVP Launch Criteria

- Users can register, verify contact details, and manage profiles
- Sellers can publish real estate and vehicle listings with photos
- Buyers can search, filter, save, and contact sellers
- Admins can moderate listings and manage reported content
- Core GDPR and safety requirements are implemented
- Monetization foundation is ready for featured listings and professional subscriptions

## Summary

The recommended launch path is to build a strong marketplace core first, then release Real Estate and Vehicles as focused verticals with category-specific fields, search filters, trust controls, and professional seller support. After the MVP is stable, monetization, SEO growth, seller analytics, and partner integrations can be added in phases.
