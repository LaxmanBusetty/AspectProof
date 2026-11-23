import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="81ebca8a-28d3-426a-9b78-bdcefad68ae3",
    name="Verify Shop Page Product Listing and Layout Report",
    tc_id="TC-53",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"product_count_check": "4", "listed_product_prices": "true", "listed_product_add_to_cart_buttons": "true", "issues_seen_this_session_check": "Issues seen this session: 0", "layout_report": "AspectProof layout\nLaptop 1280\u00d7800 (full window)\nProbe: active (76 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=laptop-1280&run=r7-laptop-1280__browse&start=%2F', instruction_id='3d216a0e-917d-48e6-af7a-3a9d506e6162'):
        await page.goto("http://localhost:4400/__ap/frame?profile=laptop-1280&run=r7-laptop-1280__browse&start=%2F")
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking the Menu button and opening the Shop page via the header link', instruction_id='f8dda70f-233a-466d-9377-d5ab050bd1eb'):
        _loc_2 = frame_0.locator("internal:role=link[name=\"Shop\"s]")
        
        await _loc_2.click()
        # Reset to main page context
    _condition_met = False
    _until_retries = 0
    while _until_retries < 10:
        print(f"[until-loop] iteration {_until_retries + 1}/10")
        async with testmu.step('Waiting for the Shop page heading to be visible', instruction_id='51db4593-44a3-474b-9ffb-025e118dd717'):
            await page.wait_for_timeout(500)
        await page.wait_for_timeout(500)
        if await testmu.check_until_condition(page, "the heading 'Shop' is visible"):
            _condition_met = True
            break
        _until_retries += 1
    set_var("__result__", {"condition_met": _condition_met, "retries": _until_retries + 1})
    
    async with testmu.step('Counting the listed product cards'):
        set_var('product_count_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {13: 0, 16: 1, 19: 2, 22: 3};\n  const el = (i) => els[__m[i]];\n  const __v = ([el(13),el(16),el(19),el(22)].filter(Boolean).length);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Daypack 22L $89.00 Add to cart"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Storm Shell Jacket $189.00"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Merino Trail Tee $59.00 Add"i'], query='the number of distinct listed product article cards', expected_value='3', needs_unit_conversion=False, operator='gte', transforms=[], condition='At least 3 products are listed.'))
    
    async with testmu.step('Checking whether listed products have prices'):
        set_var('listed_product_prices', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {13: 0, 16: 1, 19: 2, 22: 3};\n  const el = (i) => els[__m[i]];\n  const __v = ([el(13),el(16),el(19),el(22)].every(card => /\\$\\d+(?:\\.\\d{2})?/.test(card.innerText)));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Daypack 22L $89.00 Add to cart"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Storm Shell Jacket $189.00"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Merino Trail Tee $59.00 Add"i'], query='whether prices for each listed product are present in the product article cards', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='Each listed product has a price.'))
    
    async with testmu.step('Checking whether listed products have Add to cart buttons'):
        set_var('listed_product_add_to_cart_buttons', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {13: 0, 16: 1, 19: 2, 22: 3};\n  const el = (i) => els[__m[i]];\n  const __v = ([el(13),el(16),el(19),el(22)].every(card => Array.from(card.querySelectorAll('button')).some(button => button.innerText.trim() === 'Add to cart')));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Daypack 22L $89.00 Add to cart"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Storm Shell Jacket $189.00"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Merino Trail Tee $59.00 Add"i'], query='whether Add to cart buttons for each listed product are present in the product article cards', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="Each listed product has an 'Add to cart' button."))
    
    async with testmu.step('Reading the session issue count from the layout panel'):
        set_var('issues_seen_this_session_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {31: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(31).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Issues seen this session:"i'], query='the Issues seen this session text in the AspectProof layout panel', expected_value='Issues seen this session: 0', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The "AspectProof layout" panel shows "Issues seen this session: 0".'))
    
    async with testmu.step('Reading the full AspectProof layout report'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {28: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(28).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The full panel text is stored as {{layout_report}}.'))
    
    async with testmu.step('Assertion check', instruction_id='6d09d736-3c41-44e7-91bb-85d412f2f9c3'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'At least 3 products are listed.', 'passed': True, 'operator': 'gte', 'transforms': [], 'json_path': None, 'expected': '3', 'extracted_value': '{{product_count_check}}', 'store_key': 'product_count_check', 'variable_refs': {'{{product_count_check}}': '4'}}, {'description': 'Each listed product has a price.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{listed_product_prices}}', 'store_key': 'listed_product_prices', 'variable_refs': {'{{listed_product_prices}}': 'true'}}, {'description': "Each listed product has an 'Add to cart' button.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{listed_product_add_to_cart_buttons}}', 'store_key': 'listed_product_add_to_cart_buttons', 'variable_refs': {'{{listed_product_add_to_cart_buttons}}': 'true'}}], 'sub_checks': [{'description': 'At least 3 products are listed.', 'store_key': 'product_count_check', 'expected_value': '3', 'extracted_value': '{{product_count_check}}', 'operator': 'gte', 'transforms': []}, {'description': 'Each listed product has a price.', 'store_key': 'listed_product_prices', 'expected_value': 'true', 'extracted_value': '{{listed_product_prices}}', 'operator': 'equals', 'transforms': []}, {'description': "Each listed product has an 'Add to cart' button.", 'store_key': 'listed_product_add_to_cart_buttons', 'expected_value': 'true', 'extracted_value': '{{listed_product_add_to_cart_buttons}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "At least 3 products are listed, each with a price and an 'Add to cart' button."})
    
    async with testmu.step('Assertion check', instruction_id='41a6e2ec-b526-4e4d-9e8f-e47ae5c6e0b8'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'passed': True, 'operator': 'equals', 'transforms': ['strip'], 'json_path': None, 'expected': 'Issues seen this session: 0', 'extracted_value': '{{issues_seen_this_session_check}}', 'store_key': 'issues_seen_this_session_check', 'variable_refs': {'{{issues_seen_this_session_check}}': 'Issues seen this session: 0'}}], 'sub_checks': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'store_key': 'issues_seen_this_session_check', 'expected_value': 'Issues seen this session: 0', 'extracted_value': '{{issues_seen_this_session_check}}', 'operator': 'equals', 'transforms': ['strip']}], 'composite_operator': 'and', 'claim': 'The "AspectProof layout" panel shows "Issues seen this session: 0".'})


if __name__ == "__main__":
    testmu.run(test)