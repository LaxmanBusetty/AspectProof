import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="3097b09b-22fd-4e78-aadd-01631fb06e42",
    name="Verify Shop Page Product Listing and Layout Status",
    tc_id="TC-8",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"product_count_check": "4", "product_prices_present": "true", "add_to_cart_buttons_present": "true", "layout_issues_session_check": "true", "layout_report": "AspectProof layout\nLaptop 1280\u00d7800 (full window)\nProbe: active (93 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=laptop-1280&run=r3-laptop-1280__browse&start=%2F', instruction_id='1a06d960-8761-4b77-b60e-387d6eff1791'):
        await page.goto("http://localhost:4400/__ap/frame?profile=laptop-1280&run=r3-laptop-1280__browse&start=%2F")
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Shop in the header navigation', instruction_id='73a4255e-6f25-407e-a02f-8f10512ceaec'):
        _loc_2 = frame_0.locator("internal:role=link[name=\"Shop\"s]")
        
        await _loc_2.click()
        # Reset to main page context
    _condition_met = False
    _until_retries = 0
    while _until_retries < 10:
        print(f"[until-loop] iteration {_until_retries + 1}/10")
        async with testmu.step('Waiting for Shop page heading to be visible', instruction_id='b2aa5eb1-b929-42a4-912c-c6c931538a18'):
            await page.wait_for_timeout(500)
        await page.wait_for_timeout(500)
        if await testmu.check_until_condition(page, 'the heading "Shop" is visible'):
            _condition_met = True
            break
        _until_retries += 1
    set_var("__result__", {"condition_met": _condition_met, "retries": _until_retries + 1})
    
    async with testmu.step('Counting products in the shop listing'):
        set_var('product_count_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {12: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(12).querySelectorAll('article').length);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query='the number of product cards in the shop product listing', expected_value='3', needs_unit_conversion=False, operator='gte', transforms=[], condition='At least 3 products are listed.'))
    
    async with testmu.step('Checking whether product prices are present'):
        set_var('product_prices_present', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {12: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(12).querySelectorAll('article')).every(card => /(?:\\$|€|£)\\s*\\d+(?:[.,]\\d{2})?/.test(card.innerText)));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query='whether every product card in the shop product listing displays a price', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='Each listed product has a price.'))
    
    async with testmu.step('Checking whether Add to cart buttons are present'):
        set_var('add_to_cart_buttons_present', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {12: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(12).querySelectorAll('article')).every(card => Array.from(card.querySelectorAll('button')).some(button => button.innerText.trim() === 'Add to cart')));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query='whether every product card in the shop product listing has an Add to cart button', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="Each listed product has an 'Add to cart' button."))
    
    async with testmu.step('Assertion check', instruction_id='ea5279fe-02c8-4fdd-84b9-366a96bb0a08'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'At least 3 products are listed.', 'passed': True, 'operator': 'gte', 'transforms': [], 'json_path': None, 'expected': '3', 'extracted_value': '{{product_count_check}}', 'store_key': 'product_count_check', 'variable_refs': {'{{product_count_check}}': '4'}}, {'description': 'Each listed product has a price.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{product_prices_present}}', 'store_key': 'product_prices_present', 'variable_refs': {'{{product_prices_present}}': 'true'}}, {'description': "Each listed product has an 'Add to cart' button.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{add_to_cart_buttons_present}}', 'store_key': 'add_to_cart_buttons_present', 'variable_refs': {'{{add_to_cart_buttons_present}}': 'true'}}], 'sub_checks': [{'description': 'At least 3 products are listed.', 'store_key': 'product_count_check', 'expected_value': '3', 'extracted_value': '{{product_count_check}}', 'operator': 'gte', 'transforms': []}, {'description': 'Each listed product has a price.', 'store_key': 'product_prices_present', 'expected_value': 'true', 'extracted_value': '{{product_prices_present}}', 'operator': 'equals', 'transforms': []}, {'description': "Each listed product has an 'Add to cart' button.", 'store_key': 'add_to_cart_buttons_present', 'expected_value': 'true', 'extracted_value': '{{add_to_cart_buttons_present}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "At least 3 products are listed, each with a price and an 'Add to cart' button."})
    
    async with testmu.step('Checking whether the session issues text is present'):
        set_var('layout_issues_session_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {28: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (/Issues seen this session:\\s*0/.test(el(28).innerText));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='whether the text “Issues seen this session: 0” is present in the AspectProof layout panel', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='The "AspectProof layout" panel shows "Issues seen this session: 0".'))
    
    async with testmu.step('Reading the AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {28: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(28).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The full panel text is stored as {{layout_report}}.'))
    
    async with testmu.step('Assertion check', instruction_id='15c563c0-3031-4047-912d-ac1668d42fa0'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{layout_issues_session_check}}', 'store_key': 'layout_issues_session_check', 'variable_refs': {'{{layout_issues_session_check}}': 'true'}}], 'sub_checks': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'store_key': 'layout_issues_session_check', 'expected_value': 'true', 'extracted_value': '{{layout_issues_session_check}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'The "AspectProof layout" panel shows "Issues seen this session: 0".'})


if __name__ == "__main__":
    testmu.run(test)