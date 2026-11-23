import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="66dbfedf-22bc-48ad-a51b-50f639f7ea20",
    name="Verify Shop Page and Layout Panel on Small Screen",
    tc_id="TC-68",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"shop_product_count_check": "4", "listed_product_prices_present": "true", "listed_product_add_to_cart_buttons_present": "true", "aspectproof_issues_seen_this_session_check": "true", "layout_report": "AspectProof layout\nPhone 320\u00d7568 (small Android) \u00b7 portrait\nProbe: active (76 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=phone-320&run=r7-phone-320__browse&start=%2F', instruction_id='c1a2fc82-1bef-401a-9ff1-2d5ac86541d6'):
        await page.goto("http://localhost:4400/__ap/frame?profile=phone-320&run=r7-phone-320__browse&start=%2F")
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking the Menu button in the top-right corner', instruction_id='1e4d990d-6208-4fd0-8fb0-dc5c26ed55f3'):
        _loc_2 = frame_0.locator("internal:role=button[name=\"Menu\"i]")
        
        await _loc_2.click()
        # Reset to main page context
        frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking the Shop link in the header navigation menu', instruction_id='97311ddf-7725-4994-a15f-d3af6d9b752c'):
        _loc_4 = frame_2.locator("internal:role=link[name=\"Shop\"s]")
        
        await _loc_4.click()
        # Reset to main page context
    _condition_met = False
    _until_retries = 0
    while _until_retries < 10:
        print(f"[until-loop] iteration {_until_retries + 1}/10")
        async with testmu.step('Waiting for the Shop page to load', instruction_id='c421e367-99f0-419f-856c-ac7b9751bb3b'):
            await page.wait_for_timeout(1000)
        await page.wait_for_timeout(500)
        if await testmu.check_until_condition(page, "the heading 'Shop' is visible"):
            _condition_met = True
            break
        _until_retries += 1
    set_var("__result__", {"condition_met": _condition_met, "retries": _until_retries + 1})
    
    async with testmu.step('Counting products in the listing'):
        set_var('shop_product_count_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {9: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(9).querySelectorAll('article').length);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query='the number of product articles in the product listing', expected_value='3', needs_unit_conversion=False, operator='gte', transforms=[], condition='at least 3 products are listed'))
    
    async with testmu.step('Checking whether listed products have prices'):
        set_var('listed_product_prices_present', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {9: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(9).querySelectorAll('article')).every(article => /\\$\\d+(?:\\.\\d{2})?/.test(article.innerText)));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query='whether a price is present in each product article in the product listing', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='each listed product has a price'))
    
    async with testmu.step('Checking whether listed products have Add to cart buttons'):
        set_var('listed_product_add_to_cart_buttons_present', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {9: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(9).querySelectorAll('article')).every(article => Array.from(article.querySelectorAll('button')).some(button => button.innerText.trim() === 'Add to cart')));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query='whether an Add to cart button is present in each product article in the product listing', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="each listed product has an 'Add to cart' button"))
    
    async with testmu.step('Checking the session issue count in the AspectProof layout panel'):
        set_var('aspectproof_issues_seen_this_session_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {25: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (/Issues seen this session:\\s*0/.test(el(25).innerText));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='whether the text "Issues seen this session: 0" is present in the AspectProof layout panel', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the "AspectProof layout" panel shows "Issues seen this session: 0"'))
    
    async with testmu.step('Reading the AspectProof layout panel'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {25: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(25).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the full "AspectProof layout" panel text is stored as {{layout_report}}'))
    
    async with testmu.step('Assertion check', instruction_id='6b42accc-8f9b-4603-9079-d69547465524'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'at least 3 products are listed', 'passed': True, 'operator': 'gte', 'transforms': [], 'json_path': None, 'expected': '3', 'extracted_value': '{{shop_product_count_check}}', 'store_key': 'shop_product_count_check', 'variable_refs': {'{{shop_product_count_check}}': '4'}}, {'description': 'each listed product has a price', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{listed_product_prices_present}}', 'store_key': 'listed_product_prices_present', 'variable_refs': {'{{listed_product_prices_present}}': 'true'}}, {'description': "each listed product has an 'Add to cart' button", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{listed_product_add_to_cart_buttons_present}}', 'store_key': 'listed_product_add_to_cart_buttons_present', 'variable_refs': {'{{listed_product_add_to_cart_buttons_present}}': 'true'}}], 'sub_checks': [{'description': 'at least 3 products are listed', 'store_key': 'shop_product_count_check', 'expected_value': '3', 'extracted_value': '{{shop_product_count_check}}', 'operator': 'gte', 'transforms': []}, {'description': 'each listed product has a price', 'store_key': 'listed_product_prices_present', 'expected_value': 'true', 'extracted_value': '{{listed_product_prices_present}}', 'operator': 'equals', 'transforms': []}, {'description': "each listed product has an 'Add to cart' button", 'store_key': 'listed_product_add_to_cart_buttons_present', 'expected_value': 'true', 'extracted_value': '{{listed_product_add_to_cart_buttons_present}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "at least 3 products are listed, each with a price and an 'Add to cart' button"})
    
    async with testmu.step('Assertion check', instruction_id='63a8138b-d38a-45c9-9964-f3a678799ec7'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{aspectproof_issues_seen_this_session_check}}', 'store_key': 'aspectproof_issues_seen_this_session_check', 'variable_refs': {'{{aspectproof_issues_seen_this_session_check}}': 'true'}}], 'sub_checks': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'store_key': 'aspectproof_issues_seen_this_session_check', 'expected_value': 'true', 'extracted_value': '{{aspectproof_issues_seen_this_session_check}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the "AspectProof layout" panel shows "Issues seen this session: 0"'})


if __name__ == "__main__":
    testmu.run(test)