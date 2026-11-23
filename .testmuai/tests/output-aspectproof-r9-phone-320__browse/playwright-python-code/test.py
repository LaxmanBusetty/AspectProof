import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="05fe96e7-cf03-4128-b013-3a737160f266",
    name="Verify Shop Page Product Listings and Layout Report",
    tc_id="TC-93",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"product_listing_count_check": "4", "first_listed_product_price": "true", "first_listed_product_add_to_cart_button": "true", "second_listed_product_price": "true", "second_listed_product_add_to_cart_button": "true", "third_listed_product_price": "true", "third_listed_product_add_to_cart_button": "true", "aspectproof_issues_seen_this_session": "true", "layout_report": "AspectProof layout\nPhone 320\u00d7568 (small Android) \u00b7 portrait\nProbe: active (88 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=phone-320&run=r9-phone-320__browse&start=%2F', instruction_id='34984519-5473-4d87-863c-ad07c819659c'):
        await page.goto("http://localhost:4400/__ap/frame?profile=phone-320&run=r9-phone-320__browse&start=%2F")
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking the Menu button at the top right', instruction_id='4bd08da0-96e9-4ad0-bdc9-1657fc0f2bb9'):
        _loc_2 = frame_0.locator("internal:role=button[name=\"Menu\"i]")
        
        await _loc_2.click()
        # Reset to main page context
        frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking the Shop link in the header navigation', instruction_id='6518a017-dca8-4f64-86fa-5e03cd8cc3da'):
        _loc_4 = frame_2.locator("internal:role=link[name=\"Shop\"s]")
        
        await _loc_4.click()
        # Reset to main page context
    _condition_met = False
    _until_retries = 0
    while _until_retries < 10:
        print(f"[until-loop] iteration {_until_retries + 1}/10")
        async with testmu.step('Waiting for the Shop page heading to be visible', instruction_id='1beba803-b074-4f06-a861-b32922b6944a'):
            await page.wait_for_timeout(500)
        await page.wait_for_timeout(500)
        if await testmu.check_until_condition(page, "the heading 'Shop' is visible"):
            _condition_met = True
            break
        _until_retries += 1
    set_var("__result__", {"condition_met": _condition_met, "retries": _until_retries + 1})
    
    async with testmu.step('Counting products in the listing'):
        set_var('product_listing_count_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {9: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(9).querySelectorAll(':scope > article').length);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query='the number of product articles in the product listing', expected_value='3', needs_unit_conversion=False, operator='gte', transforms=[], condition='At least 3 products are listed.'))
    
    async with testmu.step('Checking whether the first listed product price is present'):
        set_var('first_listed_product_price', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {10: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (!!(el(10).innerText.match(/[$€£]\\s*\\d/)));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00"i'], query='whether a price for the first listed product is present in its product card', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='The first listed product has a price.'))
    
    async with testmu.step('Checking whether the first listed product Add to cart button is present'):
        set_var('first_listed_product_add_to_cart_button', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {10: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(10).querySelectorAll('button')).some(b=>b.innerText.trim()==='Add to cart'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00"i'], query='whether an Add to cart button for the first listed product is present in its product card', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="The first listed product has an 'Add to cart' button."))
    
    async with testmu.step('Checking whether the second listed product price is present'):
        set_var('second_listed_product_price', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {13: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (!!(el(13).innerText.match(/[$€£]\\s*\\d/)));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Daypack 22L $89.00 Add to cart"i'], query='whether a price for the second listed product is present in its product card', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='The second listed product has a price.'))
    
    async with testmu.step('Checking whether the second listed product Add to cart button is present'):
        set_var('second_listed_product_add_to_cart_button', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {13: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(13).querySelectorAll('button')).some(b=>b.innerText.trim()==='Add to cart'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Daypack 22L $89.00 Add to cart"i'], query='whether an Add to cart button for the second listed product is present in its product card', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="The second listed product has an 'Add to cart' button."))
    
    async with testmu.step('Checking whether the third listed product price is present'):
        set_var('third_listed_product_price', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {16: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (!!(el(16).innerText.match(/[$€£]\\s*\\d/)));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Storm Shell Jacket $189.00"i'], query='whether a price for the third listed product is present in its product card', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='The third listed product has a price.'))
    
    async with testmu.step('Checking whether the third listed product Add to cart button is present'):
        set_var('third_listed_product_add_to_cart_button', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {16: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(16).querySelectorAll('button')).some(b=>b.innerText.trim()==='Add to cart'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Storm Shell Jacket $189.00"i'], query='whether an Add to cart button for the third listed product is present in its product card', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="The third listed product has an 'Add to cart' button."))
    
    async with testmu.step('Checking whether the session issue count is present'):
        set_var('aspectproof_issues_seen_this_session', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {28: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(28).innerText.trim()==='Issues seen this session: 0');\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Issues seen this session:"i'], query='whether Issues seen this session: 0 is present in the AspectProof layout panel', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='The "AspectProof layout" panel shows "Issues seen this session: 0".'))
    
    async with testmu.step('Reading the AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {25: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(25).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The full "AspectProof layout" panel text is stored as {{layout_report}}.'))
    
    async with testmu.step('Assertion check', instruction_id='dff02eae-a63a-40b3-a708-36b6463fe54e'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'At least 3 products are listed.', 'passed': True, 'operator': 'gte', 'transforms': [], 'json_path': None, 'expected': '3', 'extracted_value': '{{product_listing_count_check}}', 'store_key': 'product_listing_count_check', 'variable_refs': {'{{product_listing_count_check}}': '4'}}, {'description': 'The first listed product has a price.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{first_listed_product_price}}', 'store_key': 'first_listed_product_price', 'variable_refs': {'{{first_listed_product_price}}': 'true'}}, {'description': "The first listed product has an 'Add to cart' button.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{first_listed_product_add_to_cart_button}}', 'store_key': 'first_listed_product_add_to_cart_button', 'variable_refs': {'{{first_listed_product_add_to_cart_button}}': 'true'}}, {'description': 'The second listed product has a price.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{second_listed_product_price}}', 'store_key': 'second_listed_product_price', 'variable_refs': {'{{second_listed_product_price}}': 'true'}}, {'description': "The second listed product has an 'Add to cart' button.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{second_listed_product_add_to_cart_button}}', 'store_key': 'second_listed_product_add_to_cart_button', 'variable_refs': {'{{second_listed_product_add_to_cart_button}}': 'true'}}, {'description': 'The third listed product has a price.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{third_listed_product_price}}', 'store_key': 'third_listed_product_price', 'variable_refs': {'{{third_listed_product_price}}': 'true'}}, {'description': "The third listed product has an 'Add to cart' button.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{third_listed_product_add_to_cart_button}}', 'store_key': 'third_listed_product_add_to_cart_button', 'variable_refs': {'{{third_listed_product_add_to_cart_button}}': 'true'}}], 'sub_checks': [{'description': 'At least 3 products are listed.', 'store_key': 'product_listing_count_check', 'expected_value': '3', 'extracted_value': '{{product_listing_count_check}}', 'operator': 'gte', 'transforms': []}, {'description': 'The first listed product has a price.', 'store_key': 'first_listed_product_price', 'expected_value': 'true', 'extracted_value': '{{first_listed_product_price}}', 'operator': 'equals', 'transforms': []}, {'description': "The first listed product has an 'Add to cart' button.", 'store_key': 'first_listed_product_add_to_cart_button', 'expected_value': 'true', 'extracted_value': '{{first_listed_product_add_to_cart_button}}', 'operator': 'equals', 'transforms': []}, {'description': 'The second listed product has a price.', 'store_key': 'second_listed_product_price', 'expected_value': 'true', 'extracted_value': '{{second_listed_product_price}}', 'operator': 'equals', 'transforms': []}, {'description': "The second listed product has an 'Add to cart' button.", 'store_key': 'second_listed_product_add_to_cart_button', 'expected_value': 'true', 'extracted_value': '{{second_listed_product_add_to_cart_button}}', 'operator': 'equals', 'transforms': []}, {'description': 'The third listed product has a price.', 'store_key': 'third_listed_product_price', 'expected_value': 'true', 'extracted_value': '{{third_listed_product_price}}', 'operator': 'equals', 'transforms': []}, {'description': "The third listed product has an 'Add to cart' button.", 'store_key': 'third_listed_product_add_to_cart_button', 'expected_value': 'true', 'extracted_value': '{{third_listed_product_add_to_cart_button}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "At least 3 products are listed, each with a price and an 'Add to cart' button."})
    
    async with testmu.step('Assertion check', instruction_id='cf8b6dfa-8022-432b-935f-3572041e9dfd'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{aspectproof_issues_seen_this_session}}', 'store_key': 'aspectproof_issues_seen_this_session', 'variable_refs': {'{{aspectproof_issues_seen_this_session}}': 'true'}}], 'sub_checks': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'store_key': 'aspectproof_issues_seen_this_session', 'expected_value': 'true', 'extracted_value': '{{aspectproof_issues_seen_this_session}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'The "AspectProof layout" panel shows "Issues seen this session: 0".'})


if __name__ == "__main__":
    testmu.run(test)