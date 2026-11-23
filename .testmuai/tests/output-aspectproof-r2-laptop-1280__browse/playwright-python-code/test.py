import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="71835f31-0af7-496a-845f-e6b602270ad8",
    name="Verify Shop Page Product Listings and Layout Panel Status",
    tc_id="TC-3",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"product_list_count_check": "4", "product_prices_present": "true", "add_to_cart_buttons_present": "true", "layout_issues_seen_check": "0", "layout_report": "AspectProof layout\nLaptop 1280\u00d7800 (full window)\nProbe: active (50 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=laptop-1280&run=r2-laptop-1280__browse&start=%2F', instruction_id='81172a74-f9de-48af-a13a-2a06b60e0631'):
        await page.goto("http://localhost:4400/__ap/frame?profile=laptop-1280&run=r2-laptop-1280__browse&start=%2F")
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking the Shop link in the header navigation', instruction_id='4701063c-6ae7-47db-8f2a-59588bf9d8cf'):
        _loc_2 = frame_0.locator("internal:role=link[name=\"Shop\"s]")
        
        await _loc_2.click()
        # Reset to main page context
    _condition_met = False
    _until_retries = 0
    while _until_retries < 10:
        print(f"[until-loop] iteration {_until_retries + 1}/10")
        async with testmu.step('Waiting for the Shop page heading to be visible', instruction_id='4c864cad-ae5c-47b5-bcbc-e7738ffb741e'):
            await page.wait_for_timeout(500)
        await page.wait_for_timeout(500)
        if await testmu.check_until_condition(page, "the heading 'Shop' is visible"):
            _condition_met = True
            break
        _until_retries += 1
    set_var("__result__", {"condition_met": _condition_met, "retries": _until_retries + 1})
    
    async with testmu.step('Counting products in the product listing'):
        set_var('product_list_count_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {13: 0, 16: 1, 19: 2, 22: 3};\n  const el = (i) => els[__m[i]];\n  const __v = ([el(13),el(16),el(19),el(22)].filter(x => x && !!x.querySelector('h3')).length);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Daypack 22L $89.00 Add to cart"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Storm Shell Jacket $189.00"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Merino Trail Tee $59.00 Add"i'], query='the count of product articles in the product listing', expected_value='3', needs_unit_conversion=False, operator='gte', transforms=[], condition='At least 3 products are listed.'))
    
    async with testmu.step('Checking whether each listed product has a price'):
        set_var('product_prices_present', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {13: 0, 16: 1, 19: 2, 22: 3};\n  const el = (i) => els[__m[i]];\n  const __v = ([el(13),el(16),el(19),el(22)].every(x => x && /[$€£]\\s*\\d/.test(x.innerText)));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Daypack 22L $89.00 Add to cart"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Storm Shell Jacket $189.00"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Merino Trail Tee $59.00 Add"i'], query='whether a price for each listed product is present in the product listing', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='Each listed product has a price.'))
    
    async with testmu.step('Checking whether each listed product has an Add to cart button'):
        set_var('add_to_cart_buttons_present', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {13: 0, 16: 1, 19: 2, 22: 3};\n  const el = (i) => els[__m[i]];\n  const __v = ([el(13),el(16),el(19),el(22)].every(x => x && Array.from(x.querySelectorAll('button')).some(b => b.innerText.trim()==='Add to cart')));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Daypack 22L $89.00 Add to cart"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Storm Shell Jacket $189.00"i', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Merino Trail Tee $59.00 Add"i'], query='whether an Add to cart button for each listed product is present in the product listing', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="Each listed product has an 'Add to cart' button."))
    
    async with testmu.step('Reading the session layout issue count'):
        set_var('layout_issues_seen_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {31: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(31).querySelector('strong')?.innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Issues seen this session:"i'], query='the Issues seen this session value in the AspectProof layout panel', expected_value='0', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The "AspectProof layout" panel shows "Issues seen this session: 0".'))
    
    async with testmu.step('Reading the AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {28: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(28).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The full panel text is stored as {{layout_report}}.'))
    
    async with testmu.step('Assertion check', instruction_id='7caccc37-25ed-4ebf-87b4-dd6fe7f31b42'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'At least 3 products are listed.', 'passed': True, 'operator': 'gte', 'transforms': [], 'json_path': None, 'expected': '3', 'extracted_value': '{{product_list_count_check}}', 'store_key': 'product_list_count_check', 'variable_refs': {'{{product_list_count_check}}': '4'}}, {'description': 'Each listed product has a price.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{product_prices_present}}', 'store_key': 'product_prices_present', 'variable_refs': {'{{product_prices_present}}': 'true'}}, {'description': "Each listed product has an 'Add to cart' button.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{add_to_cart_buttons_present}}', 'store_key': 'add_to_cart_buttons_present', 'variable_refs': {'{{add_to_cart_buttons_present}}': 'true'}}], 'sub_checks': [{'description': 'At least 3 products are listed.', 'store_key': 'product_list_count_check', 'expected_value': '3', 'extracted_value': '{{product_list_count_check}}', 'operator': 'gte', 'transforms': []}, {'description': 'Each listed product has a price.', 'store_key': 'product_prices_present', 'expected_value': 'true', 'extracted_value': '{{product_prices_present}}', 'operator': 'equals', 'transforms': []}, {'description': "Each listed product has an 'Add to cart' button.", 'store_key': 'add_to_cart_buttons_present', 'expected_value': 'true', 'extracted_value': '{{add_to_cart_buttons_present}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "At least 3 products are listed, each with a price and an 'Add to cart' button."})
    
    async with testmu.step('Assertion check', instruction_id='29b19ef7-20a6-4842-9ef7-d97c894255f9'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'passed': True, 'operator': 'equals', 'transforms': ['strip'], 'json_path': None, 'expected': '0', 'extracted_value': '{{layout_issues_seen_check}}', 'store_key': 'layout_issues_seen_check', 'variable_refs': {'{{layout_issues_seen_check}}': '0'}}], 'sub_checks': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'store_key': 'layout_issues_seen_check', 'expected_value': '0', 'extracted_value': '{{layout_issues_seen_check}}', 'operator': 'equals', 'transforms': ['strip']}], 'composite_operator': 'and', 'claim': 'The "AspectProof layout" panel shows "Issues seen this session: 0".'})


if __name__ == "__main__":
    testmu.run(test)