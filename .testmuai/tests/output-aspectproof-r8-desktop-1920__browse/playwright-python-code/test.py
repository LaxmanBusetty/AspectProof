import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="c0d9ca4a-2cbd-47b2-8d32-4b5cc9b1541d",
    name="Verify Shop Page Product Listings and Layout Status",
    tc_id="TC-74",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"shop_product_count_check": "4", "listed_products_prices_check": "true", "listed_products_add_to_cart_buttons_check": "true", "aspectproof_layout_issues_seen_session_check": "true", "layout_report": "AspectProof layout\nDesktop 1920\u00d71080 (full window)\nProbe: active (91 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=desktop-1920&run=r8-desktop-1920__browse&start=%2F', instruction_id='e7f972a3-4178-4707-8bb4-9a199947ba19'):
        await page.goto("http://localhost:4400/__ap/frame?profile=desktop-1920&run=r8-desktop-1920__browse&start=%2F")
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking the Shop link in the header navigation', instruction_id='35107067-7eb4-4a4c-990a-eb3564e70a6d'):
        _loc_2 = frame_0.locator("internal:role=link[name=\"Shop\"s]")
        
        await _loc_2.click()
        # Reset to main page context
    
    async with testmu.step('Waiting for the Shop page to display after header navigation', instruction_id='38d67366-7b61-4427-bede-cf4f1c4e14ca'):
        await page.wait_for_timeout(500)
    
    async with testmu.step('Counting products in the listing'):
        set_var('shop_product_count_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {12: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(12).querySelectorAll(':scope > article').length);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query='the number of product articles in the product listing', expected_value='3', needs_unit_conversion=False, operator='gte', transforms=[], condition='At least 3 products are listed.'))
    
    async with testmu.step('Checking whether listed products have prices'):
        set_var('listed_products_prices_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {12: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(12).querySelectorAll(':scope > article')).every(article => /(?:^|\\s)[$€£]\\s*\\d+(?:\\.\\d{2})?(?:\\s|$)/.test(article.innerText)));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query='whether a price for each listed product is present in the product listing', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='Each listed product has a price.'))
    
    async with testmu.step('Checking whether listed products have Add to cart buttons'):
        set_var('listed_products_add_to_cart_buttons_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {12: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(12).querySelectorAll(':scope > article')).every(article => Array.from(article.querySelectorAll('button')).some(button => button.innerText.trim() === 'Add to cart')));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query="whether an 'Add to cart' button for each listed product is present in the product listing", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="Each listed product has an 'Add to cart' button."))
    
    async with testmu.step('Assertion check', instruction_id='15c37a2c-4ee4-4d0c-a253-a598e0a1f2e7'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'At least 3 products are listed.', 'passed': True, 'operator': 'gte', 'transforms': [], 'json_path': None, 'expected': '3', 'extracted_value': '{{shop_product_count_check}}', 'store_key': 'shop_product_count_check', 'variable_refs': {'{{shop_product_count_check}}': '4'}}, {'description': 'Each listed product has a price.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{listed_products_prices_check}}', 'store_key': 'listed_products_prices_check', 'variable_refs': {'{{listed_products_prices_check}}': 'true'}}, {'description': "Each listed product has an 'Add to cart' button.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{listed_products_add_to_cart_buttons_check}}', 'store_key': 'listed_products_add_to_cart_buttons_check', 'variable_refs': {'{{listed_products_add_to_cart_buttons_check}}': 'true'}}], 'sub_checks': [{'description': 'At least 3 products are listed.', 'store_key': 'shop_product_count_check', 'expected_value': '3', 'extracted_value': '{{shop_product_count_check}}', 'operator': 'gte', 'transforms': []}, {'description': 'Each listed product has a price.', 'store_key': 'listed_products_prices_check', 'expected_value': 'true', 'extracted_value': '{{listed_products_prices_check}}', 'operator': 'equals', 'transforms': []}, {'description': "Each listed product has an 'Add to cart' button.", 'store_key': 'listed_products_add_to_cart_buttons_check', 'expected_value': 'true', 'extracted_value': '{{listed_products_add_to_cart_buttons_check}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "At least 3 products are listed, each with a price and an 'Add to cart' button."})
    
    async with testmu.step('Waiting while reading the full text in the AspectProof layout panel', instruction_id='327600a5-2a0f-47e9-90e0-f2c37ce7e4f3'):
        await page.wait_for_timeout(500)
    
    async with testmu.step('Checking the session issue count in the AspectProof layout panel'):
        set_var('aspectproof_layout_issues_seen_session_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {28: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (/^Issues seen this session:\\s*0\\s*$/m.test(el(28).innerText));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='whether the AspectProof layout panel reports Issues seen this session as 0', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='The "AspectProof layout" panel shows "Issues seen this session: 0".'))
    
    async with testmu.step('Reading the full AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {28: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(28).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The full panel text is stored as layout_report.'))
    
    async with testmu.step('Assertion check', instruction_id='6a158f6a-b9e9-4aaf-b98c-6a7282d2ced8'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{aspectproof_layout_issues_seen_session_check}}', 'store_key': 'aspectproof_layout_issues_seen_session_check', 'variable_refs': {'{{aspectproof_layout_issues_seen_session_check}}': 'true'}}], 'sub_checks': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'store_key': 'aspectproof_layout_issues_seen_session_check', 'expected_value': 'true', 'extracted_value': '{{aspectproof_layout_issues_seen_session_check}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'The "AspectProof layout" panel shows "Issues seen this session: 0".'})


if __name__ == "__main__":
    testmu.run(test)