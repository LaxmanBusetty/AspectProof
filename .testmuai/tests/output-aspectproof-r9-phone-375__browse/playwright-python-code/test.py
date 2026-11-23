import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="4940b94c-b376-4381-91d0-aef86a16e5df",
    name="Verify Shop Page Product Listings and Layout Panel Status",
    tc_id="TC-90",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"product_count_check": "4", "product_price_present": "true", "add_to_cart_button_present": "true", "aspectproof_issues_seen_this_session": "true", "layout_report": "AspectProof layout\nPhone 375\u00d7812 (iPhone 11 Pro) \u00b7 portrait\nProbe: active (68 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=phone-375&run=r9-phone-375__browse&start=%2F', instruction_id='b1179945-a3f1-4062-8fb4-aab52622b177'):
        await page.goto("http://localhost:4400/__ap/frame?profile=phone-375&run=r9-phone-375__browse&start=%2F")
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking the Menu button in the top right', instruction_id='2d9bb478-89cf-43db-817d-b87055a5db13'):
        _loc_2 = frame_0.locator("internal:role=button[name=\"Menu\"i]")
        
        await _loc_2.click()
        # Reset to main page context
        frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking the Shop link in the top-right header menu', instruction_id='5700adf7-402c-4f7a-addb-f4e8ad153483'):
        _loc_4 = frame_2.locator("internal:role=link[name=\"Shop\"s]")
        
        await _loc_4.click()
        # Reset to main page context
    _condition_met = False
    _until_retries = 0
    while _until_retries < 10:
        print(f"[until-loop] iteration {_until_retries + 1}/10")
        async with testmu.step('Waiting for the Shop page heading to become visible', instruction_id='d9b5afe2-0515-4824-aed0-153f3cd50b17'):
            await page.wait_for_timeout(500)
        await page.wait_for_timeout(500)
        if await testmu.check_until_condition(page, 'the heading "Shop" is visible'):
            _condition_met = True
            break
        _until_retries += 1
    set_var("__result__", {"condition_met": _condition_met, "retries": _until_retries + 1})
    
    async with testmu.step('Counting listed products'):
        set_var('product_count_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {7: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(7).querySelectorAll('article').length);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Shop Trail Runner Shoes $129."i'], query='the number of listed product articles in the Shop content area', expected_value='3', needs_unit_conversion=False, operator='gte', transforms=[], condition='At least 3 products are listed.'))
    
    async with testmu.step('Checking whether each listed product has a price'):
        set_var('product_price_present', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {7: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(7).querySelectorAll('article')).every(card => /[$€£]\\s?\\d+(?:\\.\\d{2})?/.test(card.innerText)));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Shop Trail Runner Shoes $129."i'], query='whether a price for each listed product is present in the Shop content area', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='Each listed product has a price.'))
    
    async with testmu.step('Checking whether each listed product has an Add to cart button'):
        set_var('add_to_cart_button_present', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {7: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(7).querySelectorAll('article')).every(card => Array.from(card.querySelectorAll('button')).some(button => button.innerText.trim() === 'Add to cart')));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Shop Trail Runner Shoes $129."i'], query='whether an Add to cart button for each listed product is present in the Shop content area', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="Each listed product has an 'Add to cart' button."))
    
    async with testmu.step('Checking the AspectProof session issues count'):
        set_var('aspectproof_issues_seen_this_session', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {28: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(28).innerText.replace(/\\s+/g,' ').trim() === 'Issues seen this session: 0');\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Issues seen this session:"i'], query='whether "Issues seen this session: 0" in the "AspectProof layout" panel is present', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='The "AspectProof layout" panel shows "Issues seen this session: 0".'))
    
    async with testmu.step('Reading the AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {25: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(25).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The full "AspectProof layout" panel text is stored as {{layout_report}}.'))
    
    async with testmu.step('Assertion check', instruction_id='d2918304-8650-4825-8231-c797607ac4d0'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'At least 3 products are listed.', 'passed': True, 'operator': 'gte', 'transforms': [], 'json_path': None, 'expected': '3', 'extracted_value': '{{product_count_check}}', 'store_key': 'product_count_check', 'variable_refs': {'{{product_count_check}}': '4'}}, {'description': 'Each listed product has a price.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{product_price_present}}', 'store_key': 'product_price_present', 'variable_refs': {'{{product_price_present}}': 'true'}}, {'description': "Each listed product has an 'Add to cart' button.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{add_to_cart_button_present}}', 'store_key': 'add_to_cart_button_present', 'variable_refs': {'{{add_to_cart_button_present}}': 'true'}}], 'sub_checks': [{'description': 'At least 3 products are listed.', 'store_key': 'product_count_check', 'expected_value': '3', 'extracted_value': '{{product_count_check}}', 'operator': 'gte', 'transforms': []}, {'description': 'Each listed product has a price.', 'store_key': 'product_price_present', 'expected_value': 'true', 'extracted_value': '{{product_price_present}}', 'operator': 'equals', 'transforms': []}, {'description': "Each listed product has an 'Add to cart' button.", 'store_key': 'add_to_cart_button_present', 'expected_value': 'true', 'extracted_value': '{{add_to_cart_button_present}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "at least 3 products are listed, each with a price and an 'Add to cart' button."})
    
    async with testmu.step('Assertion check', instruction_id='3999b22c-3400-446f-8d14-16d29ec42c0c'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{aspectproof_issues_seen_this_session}}', 'store_key': 'aspectproof_issues_seen_this_session', 'variable_refs': {'{{aspectproof_issues_seen_this_session}}': 'true'}}], 'sub_checks': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'store_key': 'aspectproof_issues_seen_this_session', 'expected_value': 'true', 'extracted_value': '{{aspectproof_issues_seen_this_session}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the "AspectProof layout" panel shows "Issues seen this session: 0".'})


if __name__ == "__main__":
    testmu.run(test)