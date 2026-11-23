import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="df45538d-6be9-4357-a78a-f1fc6baaf0e0",
    name="Verify Shop Page Product Listing and Layout Panel Status",
    tc_id="TC-62",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"product_listing_count_check": "4", "product_prices_present": "true", "add_to_cart_buttons_present": "true", "issues_seen_this_session_check": "0", "layout_report": "AspectProof layout\nPhone 390\u00d7844 (iPhone 14) \u00b7 portrait\nProbe: active (88 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=phone-390&run=r7-phone-390__browse&start=%2F', instruction_id='cc8a30bc-ac35-450c-8a82-0b6808a0438d'):
        await page.goto("http://localhost:4400/__ap/frame?profile=phone-390&run=r7-phone-390__browse&start=%2F")
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking the Menu button in the top-right header', instruction_id='8c21735d-0394-42cd-9e3a-cb17629610c4'):
        _loc_2 = frame_0.locator("internal:role=button[name=\"Menu\"i]")
        
        await _loc_2.click()
        # Reset to main page context
        frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking the Shop link in the header navigation', instruction_id='1a3f9f92-8e99-4ed1-9a81-387823143b02'):
        _loc_4 = frame_2.locator("internal:role=link[name=\"Shop\"s]")
        
        await _loc_4.click()
        # Reset to main page context
    _condition_met = False
    _until_retries = 0
    while _until_retries < 10:
        print(f"[until-loop] iteration {_until_retries + 1}/10")
        async with testmu.step('Waiting for the Shop page to load', instruction_id='86d49e96-d5bd-46a8-9dec-d0a723124b80'):
            await page.wait_for_timeout(500)
        await page.wait_for_timeout(500)
        if await testmu.check_until_condition(page, "the heading 'Shop' is visible"):
            _condition_met = True
            break
        _until_retries += 1
    set_var("__result__", {"condition_met": _condition_met, "retries": _until_retries + 1})
    
    async with testmu.step('Counting products in the listing'):
        set_var('product_listing_count_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {10: 0, 13: 1, 16: 2, 19: 3};\n  const el = (i) => els[__m[i]];\n  const __v = ([el(10),el(13),el(16),el(19)].length);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Daypack 22L $89.00 Add to cart"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Storm Shell Jacket $189.00"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Merino Trail Tee $59.00 Add"i'], query='the number of product articles in the product listing', expected_value='3', needs_unit_conversion=False, operator='gte', transforms=[], condition='At least 3 products are listed.'))
    
    async with testmu.step('Checking whether every listed product has a price'):
        set_var('product_prices_present', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {10: 0, 13: 1, 16: 2, 19: 3};\n  const el = (i) => els[__m[i]];\n  const __v = ([el(10),el(13),el(16),el(19)].every(article => /\\$\\d+(?:\\.\\d{2})?/.test(article.innerText)));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Daypack 22L $89.00 Add to cart"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Storm Shell Jacket $189.00"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Merino Trail Tee $59.00 Add"i'], query='whether a price for each listed product is present in the product listing', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='Each listed product has a price.'))
    
    async with testmu.step('Checking whether every listed product has an Add to cart button'):
        set_var('add_to_cart_buttons_present', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {10: 0, 13: 1, 16: 2, 19: 3};\n  const el = (i) => els[__m[i]];\n  const __v = ([el(10),el(13),el(16),el(19)].every(article => Array.from(article.querySelectorAll('button')).some(button => button.innerText.trim() === 'Add to cart')));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Daypack 22L $89.00 Add to cart"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Storm Shell Jacket $189.00"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Merino Trail Tee $59.00 Add"i'], query='whether an Add to cart button for each listed product is present in the product listing', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="Each listed product has an 'Add to cart' button."))
    
    async with testmu.step('Assertion check', instruction_id='84879594-d087-4896-96b5-a30393658712'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'At least 3 products are listed.', 'passed': True, 'operator': 'gte', 'transforms': [], 'json_path': None, 'expected': '3', 'extracted_value': '{{product_listing_count_check}}', 'store_key': 'product_listing_count_check', 'variable_refs': {'{{product_listing_count_check}}': '4'}}, {'description': 'Each listed product has a price.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{product_prices_present}}', 'store_key': 'product_prices_present', 'variable_refs': {'{{product_prices_present}}': 'true'}}, {'description': "Each listed product has an 'Add to cart' button.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{add_to_cart_buttons_present}}', 'store_key': 'add_to_cart_buttons_present', 'variable_refs': {'{{add_to_cart_buttons_present}}': 'true'}}], 'sub_checks': [{'description': 'At least 3 products are listed.', 'store_key': 'product_listing_count_check', 'expected_value': '3', 'extracted_value': '{{product_listing_count_check}}', 'operator': 'gte', 'transforms': []}, {'description': 'Each listed product has a price.', 'store_key': 'product_prices_present', 'expected_value': 'true', 'extracted_value': '{{product_prices_present}}', 'operator': 'equals', 'transforms': []}, {'description': "Each listed product has an 'Add to cart' button.", 'store_key': 'add_to_cart_buttons_present', 'expected_value': 'true', 'extracted_value': '{{add_to_cart_buttons_present}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "At least 3 products are listed, each with a price and an 'Add to cart' button."})
    
    async with testmu.step('Reading the session issue count from the AspectProof layout panel'):
        set_var('issues_seen_this_session_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {29: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(29).textContent.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['#ap-seen'], query='the Issues seen this session count in the AspectProof layout panel', expected_value='0', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The "AspectProof layout" panel shows "Issues seen this session: 0".'))
    
    async with testmu.step('Extracting the AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {25: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(25).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The full "AspectProof layout" panel text is stored as {{layout_report}}.'))
    
    async with testmu.step('Assertion check', instruction_id='781a018d-dd58-416d-b577-63a3956de6f4'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'passed': True, 'operator': 'equals', 'transforms': ['strip'], 'json_path': None, 'expected': '0', 'extracted_value': '{{issues_seen_this_session_check}}', 'store_key': 'issues_seen_this_session_check', 'variable_refs': {'{{issues_seen_this_session_check}}': '0'}}], 'sub_checks': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'store_key': 'issues_seen_this_session_check', 'expected_value': '0', 'extracted_value': '{{issues_seen_this_session_check}}', 'operator': 'equals', 'transforms': ['strip']}], 'composite_operator': 'and', 'claim': 'The "AspectProof layout" panel shows "Issues seen this session: 0".'})


if __name__ == "__main__":
    testmu.run(test)