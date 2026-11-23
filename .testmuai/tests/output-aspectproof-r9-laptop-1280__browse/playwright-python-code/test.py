import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="400d9595-b7ac-42f6-ac07-7b088ef42131",
    name="Verify Shop Page Product Listing and Layout Status",
    tc_id="TC-78",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"product_count_check": "4", "listed_product_prices": "true", "listed_product_add_to_cart_buttons": "true", "issues_seen_this_session_check": "true", "layout_report": "AspectProof layout\nLaptop 1280\u00d7800 (full window)\nProbe: active (96 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=laptop-1280&run=r9-laptop-1280__browse&start=%2F', instruction_id='02594012-daad-4635-a619-3e32e7a95077'):
        await page.goto("http://localhost:4400/__ap/frame?profile=laptop-1280&run=r9-laptop-1280__browse&start=%2F")
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking the Shop link in the header navigation', instruction_id='d3c77075-6599-4967-856d-62b6b366cf9b'):
        _loc_2 = frame_0.locator("internal:role=link[name=\"Shop\"s]")
        
        await _loc_2.click()
        # Reset to main page context
    _condition_met = False
    _until_retries = 0
    while _until_retries < 10:
        print(f"[until-loop] iteration {_until_retries + 1}/10")
        async with testmu.step('Waiting for the Shop page heading to be visible', instruction_id='165e15a4-6667-4de2-b3d4-32540a3692e3'):
            await page.wait_for_timeout(500)
        await page.wait_for_timeout(500)
        if await testmu.check_until_condition(page, "the heading 'Shop' is visible"):
            _condition_met = True
            break
        _until_retries += 1
    set_var("__result__", {"condition_met": _condition_met, "retries": _until_retries + 1})
    
    async with testmu.step('Counting listed products in the shop'):
        set_var('product_count_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {14: 0, 17: 1, 20: 2, 23: 3};\n  const el = (i) => els[__m[i]];\n  const __v = ([el(14),el(17),el(20),el(23)].filter(h=>h && h.innerText.trim().length>0).length);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:role=heading[name="Trail Runner Shoes"i]', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:role=heading[name="Daypack 22L"i]', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:role=heading[name="Storm Shell Jacket"i]', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:role=heading[name="Merino Trail Tee"i]'], query='the count of listed product headings in the shop', expected_value='3', needs_unit_conversion=False, operator='gte', transforms=[], condition='At least 3 products are listed.'))
    
    async with testmu.step('whether each visible product card in the shop has a price displayed beneath its product name', instruction_id='7e3f7741-69ca-4773-8af8-fa71bda8c0a9'):
        set_var('listed_product_prices', await testmu.vision_query(page, "whether each visible product card in the shop has a price displayed beneath its product name", ""))
    
    async with testmu.step('Checking whether listed products have Add to cart buttons'):
        set_var('listed_product_add_to_cart_buttons', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {15: 0, 18: 1, 21: 2, 24: 3};\n  const el = (i) => els[__m[i]];\n  const __v = ([el(15),el(18),el(21),el(24)].every(b=>b && b.innerText.trim()==='Add to cart'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:role=article >> internal:has-text="Trail Runner Shoes $129.00"i >> internal:role=button', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:role=article >> internal:has-text="Daypack 22L $89.00 Add to cart"i >> internal:role=button', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:role=article >> internal:has-text="Storm Shell Jacket $189.00"i >> internal:role=button', 'iframe[title="App under test"] >> internal:control=enter-frame >> internal:role=article >> internal:has-text="Merino Trail Tee $59.00 Add"i >> internal:role=button'], query='whether each listed product card has an Add to cart button in the shop', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="Each listed product has an 'Add to cart' button."))
    
    async with testmu.step('Reading the session issue count from the layout panel'):
        set_var('issues_seen_this_session_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {28: 0};\n  const el = (i) => els[__m[i]];\n  const __v = ((/Issues seen this session:\\s*0(?:\\s|$)/.test(el(28).innerText)));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='whether the AspectProof layout panel reports Issues seen this session as 0', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='The "AspectProof layout" panel shows "Issues seen this session: 0".'))
    
    async with testmu.step('Extracting the AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {28: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(28).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The full panel text is stored as {{layout_report}}.'))
    
    async with testmu.step('Assertion check', instruction_id='0d78c8a4-4286-4ed9-ae82-633ea3324ece'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'At least 3 products are listed.', 'passed': True, 'operator': 'gte', 'transforms': [], 'json_path': None, 'expected': '3', 'extracted_value': '{{product_count_check}}', 'store_key': 'product_count_check', 'variable_refs': {'{{product_count_check}}': '4'}}, {'description': 'Each listed product has a price.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{listed_product_prices}}', 'store_key': 'listed_product_prices', 'variable_refs': {'{{listed_product_prices}}': 'true'}}, {'description': "Each listed product has an 'Add to cart' button.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{listed_product_add_to_cart_buttons}}', 'store_key': 'listed_product_add_to_cart_buttons', 'variable_refs': {'{{listed_product_add_to_cart_buttons}}': 'true'}}], 'sub_checks': [{'description': 'At least 3 products are listed.', 'store_key': 'product_count_check', 'expected_value': '3', 'extracted_value': '{{product_count_check}}', 'operator': 'gte', 'transforms': []}, {'description': 'Each listed product has a price.', 'store_key': 'listed_product_prices', 'expected_value': 'true', 'extracted_value': '{{listed_product_prices}}', 'operator': 'equals', 'transforms': []}, {'description': "Each listed product has an 'Add to cart' button.", 'store_key': 'listed_product_add_to_cart_buttons', 'expected_value': 'true', 'extracted_value': '{{listed_product_add_to_cart_buttons}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "At least 3 products are listed, each with a price and an 'Add to cart' button."})
    
    async with testmu.step('Assertion check', instruction_id='609ebca6-588c-4081-ad27-52affe5bea64'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{issues_seen_this_session_check}}', 'store_key': 'issues_seen_this_session_check', 'variable_refs': {'{{issues_seen_this_session_check}}': 'true'}}], 'sub_checks': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'store_key': 'issues_seen_this_session_check', 'expected_value': 'true', 'extracted_value': '{{issues_seen_this_session_check}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'The "AspectProof layout" panel shows "Issues seen this session: 0".'})


if __name__ == "__main__":
    testmu.run(test)