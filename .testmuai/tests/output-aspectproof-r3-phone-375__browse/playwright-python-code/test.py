import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="3ca6e9d1-becf-4e57-809f-490aa41f5740",
    name="Verify Shop Page Product Listings and Layout Panel Status",
    tc_id="TC-20",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"header_navigation_links_visible": "false", "shop_product_count_check": "4", "listed_products_price_present": "true", "listed_products_add_to_cart_button_present": "true", "aspectproof_issues_seen_this_session": "true", "layout_report": "AspectProof layout\nPhone 375\u00d7812 (iPhone 11 Pro) \u00b7 portrait\nProbe: active (113 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=phone-375&run=r3-phone-375__browse&start=%2F', instruction_id='6b58da2d-72b0-4bc0-8de9-8d8453552336'):
        await page.goto("http://localhost:4400/__ap/frame?profile=phone-375&run=r3-phone-375__browse&start=%2F")
    
    async with testmu.step('whether the header navigation links are visible in the page header', instruction_id='685354bf-fb66-4290-b47a-37b95557f946'):
        set_var('header_navigation_links_visible', await testmu.vision_query(page, "whether the header navigation links are visible in the page header", ""))
    if await testmu.evaluate_branch(sub_checks=[{'description': 'the header navigation links are not visible', 'store_key': 'header_navigation_links_visible', 'expected_value': 'false', 'stored_value': '{{header_navigation_links_visible}}', 'extracted_value': '{{header_navigation_links_visible}}', 'operator': 'equals', 'transforms': []}], composite_operator="and"):
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
        
        async with testmu.step('Clicking the Menu button in the top-right header', instruction_id='137ae68c-c15d-4e41-98c7-e819df4e3096'):
            _loc_2 = frame_0.locator("internal:role=button[name=\"Menu\"i]")
            
            await _loc_2.click()
            # Reset to main page context
    frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Shop in the header navigation menu', instruction_id='ed5615a7-a207-4344-bdf5-d45fa2d81945'):
        _loc_4 = frame_2.locator("internal:role=link[name=\"Shop\"s]")
        
        await _loc_4.click()
        # Reset to main page context
    _condition_met = False
    _until_retries = 0
    while _until_retries < 10:
        print(f"[until-loop] iteration {_until_retries + 1}/10")
        async with testmu.step('Waiting for the Shop page to load', instruction_id='4dea81ee-3085-4e9c-9899-94d23d476934'):
            await page.wait_for_timeout(500)
        await page.wait_for_timeout(500)
        if await testmu.check_until_condition(page, "the heading 'Shop' is visible"):
            _condition_met = True
            break
        _until_retries += 1
    set_var("__result__", {"condition_met": _condition_met, "retries": _until_retries + 1})
    
    async with testmu.step('Counting products in the Shop listing'):
        set_var('shop_product_count_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {9: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(9).querySelectorAll(':scope > article').length);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query='the number of product articles in the Shop product listing', expected_value='3', needs_unit_conversion=False, operator='gte', transforms=[], condition='At least 3 products are listed.'))
    
    async with testmu.step('Checking prices for listed products'):
        set_var('listed_products_price_present', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {9: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(9).querySelectorAll(':scope > article')).every(article => /[$€£]\\s*\\d+(?:[.,]\\d{2})?/.test(article.innerText)));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query='whether a price for each listed product is present in the Shop product listing', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='Each listed product has a price.'))
    
    async with testmu.step('Checking Add to cart buttons for listed products'):
        set_var('listed_products_add_to_cart_button_present', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {9: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(9).querySelectorAll(':scope > article')).every(article => Array.from(article.querySelectorAll('button')).some(button => button.innerText.trim() === 'Add to cart')));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query="whether an 'Add to cart' button for each listed product is present in the Shop product listing", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="Each listed product has an 'Add to cart' button."))
    
    async with testmu.step('Assertion check', instruction_id='952c14ad-f9e5-4f08-a5c5-7982e6a94ab2'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'At least 3 products are listed.', 'passed': True, 'operator': 'gte', 'transforms': [], 'json_path': None, 'expected': '3', 'extracted_value': '{{shop_product_count_check}}', 'store_key': 'shop_product_count_check', 'variable_refs': {'{{shop_product_count_check}}': '4'}}, {'description': 'Each listed product has a price.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{listed_products_price_present}}', 'store_key': 'listed_products_price_present', 'variable_refs': {'{{listed_products_price_present}}': 'true'}}, {'description': "Each listed product has an 'Add to cart' button.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{listed_products_add_to_cart_button_present}}', 'store_key': 'listed_products_add_to_cart_button_present', 'variable_refs': {'{{listed_products_add_to_cart_button_present}}': 'true'}}], 'sub_checks': [{'description': 'At least 3 products are listed.', 'store_key': 'shop_product_count_check', 'expected_value': '3', 'extracted_value': '{{shop_product_count_check}}', 'operator': 'gte', 'transforms': []}, {'description': 'Each listed product has a price.', 'store_key': 'listed_products_price_present', 'expected_value': 'true', 'extracted_value': '{{listed_products_price_present}}', 'operator': 'equals', 'transforms': []}, {'description': "Each listed product has an 'Add to cart' button.", 'store_key': 'listed_products_add_to_cart_button_present', 'expected_value': 'true', 'extracted_value': '{{listed_products_add_to_cart_button_present}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "At least 3 products are listed, each with a price and an 'Add to cart' button."})
    
    async with testmu.step('Checking the issue count in the AspectProof layout panel'):
        set_var('aspectproof_issues_seen_this_session', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {25: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(25).innerText.includes('Issues seen this session: 0'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='whether the text "Issues seen this session: 0" is present in the AspectProof layout panel', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='The "AspectProof layout" panel shows "Issues seen this session: 0".'))
    
    async with testmu.step('Reading the AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {25: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(25).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The full "AspectProof layout" panel text is stored as {{layout_report}}.'))
    
    async with testmu.step('Assertion check', instruction_id='704202dc-9af8-4eb0-b300-bb061b6106e2'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{aspectproof_issues_seen_this_session}}', 'store_key': 'aspectproof_issues_seen_this_session', 'variable_refs': {'{{aspectproof_issues_seen_this_session}}': 'true'}}], 'sub_checks': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'store_key': 'aspectproof_issues_seen_this_session', 'expected_value': 'true', 'extracted_value': '{{aspectproof_issues_seen_this_session}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'The "AspectProof layout" panel shows "Issues seen this session: 0".'})


if __name__ == "__main__":
    testmu.run(test)