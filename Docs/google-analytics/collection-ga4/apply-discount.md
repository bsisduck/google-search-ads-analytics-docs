---
title: "Apply a discount to an ecommerce event"
source_url: "https://developers.google.com/analytics/devguides/collection/ga4/apply-discount?hl=en&client_type=gtag"
product: "Google Analytics 4"
section: "Collection (gtag)"
language: en
scraped_date: 2026-06-08
doc_id: "google-analytics/collection-ga4/apply-discount.md"
---
You can apply a discount to an item in an [ecommerce event](/analytics/devguides/collection/ga4/ecommerce) by adding the
`discount` parameter with the value of the discount. Don't use a percentage
for the `discount` parameter.

gtag.js
Tag Manager

Example
-------

A customer applies a discount code ("SAVE20") to an order containing three
units of one item (originally $10.00 each) and one unit of another item
(originally $22.00 each). The discount is allocated as $2 per unit for the first
item and $4.40 per unit for the second.

### Summary of the example calculation

Before sending the event, you must calculate the discounted price for each item.
Google Analytics does **not** automatically subtract the `discount` value from
the `price`.

| Item | Original Unit Price | Unit Discount | Price (parameter) | Quantity | Item Revenue |
| --- | --- | --- | --- | --- | --- |
| Blue Widget | $10.00 | $2.00 | **$8.00** | 3 | $24.00 |
| Red Widget | $22.00 | $4.40 | **$17.60** | 1 | $17.60 |
| **Total** |  |  |  |  | **$41.60** |

* **`value`** = Sum of item revenues = $24.00 + $17.60 = **$41.60**

Here's the
[`purchase`](/analytics/devguides/collection/ga4/reference/events#purchase)
event tag for this example:

```
// A user applies the coupon code "SAVE20" to their entire order.
// The order contains three units of one item type, and one unit of another item type.
gtag("event", "purchase", {
  'transaction_id': "T_12345",
  'value': 41.60,        // Total value after all discounts
  'currency': "USD",
  'coupon': "SAVE20",    // Order-level coupon code
  'items': [
    {
      'item_id': "SKU_123",
      'item_name': "Blue Widget",
      'price': 8.00,       // Unit price after discount (original 10.00 - 2.00 discount)
      'discount': 2.00,    // Unit discount
      'quantity': 3,
      'coupon': "SAVE20"   // Optional: Item-level coupon can match order-level
    },
    {
      'item_id': "SKU_456",
      'item_name': "Red Widget",
      'price': 17.60,      // Unit price after discount (original 22.00 - 4.40 discount)
      'discount': 4.40,    // Unit discount
      'quantity': 1,
      'coupon': "SAVE20"
    }
  ]
});
```

Report on the discount
----------------------

The following [dimensions and metrics](https://support.google.com/analytics/answer/9143382) allow you to [report](https://support.google.com/analytics/answer/9212670) on discount:

| Dimension or metric | Description |
| --- | --- |
| Item coupon | The coupon used to purchase an item (a product you sell). |
| Order coupon | The coupon name or code that you specify for discounted items. |
| Item discount amount | The total discount value from items only. Item discount amount = `quantity` x `discount`. |
| Item revenue | The total revenue from items only, excluding tax and shipping. Item revenue = `quantity` x `price`. |

Handle event-level and item-level discounts
-------------------------------------------

A coupon can be added to the entire order (event-level) or to a specific product
(item-level).

* Order-level: To apply a coupon to the entire transaction, add the `coupon`
  parameter at the event level (outside the `items` array).
* Item-level: To apply a coupon to a specific item, add the `coupon` parameter
  within that specific object in the `items` array.

If a coupon applies a discount to the entire order (event-level), you should
allocate that discount across the items in the event to ensure accurate
item-level reporting.

**Note:** Google Analytics treats `price` and `discount` as independent metrics. It
doesn't automatically subtract the `discount` from the `price`. To ensure your
revenue metrics are accurate, you must set the `price` parameter to the actual
price paid per unit (Original Price - Discount).

In each item object:

1. Add the `discount` parameter with the allocated unit discount value for the
   item.
2. Set the `price` to the unit price minus the allocated unit discount for the
   item.

You can also [create a custom metric](//support.google.com/analytics/answer/14239619) to report on event-level discounts.
