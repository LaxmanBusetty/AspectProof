import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="6a4d130b-6e31-49c9-903f-1178067070c5",
    name="Add Product to Cart and Place Order",
    tc_id="TC-97",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"order_confirmed_message": "true", "issues_seen_this_session": "0", "layout_report": "AspectProof layout\nTablet landscape 1024\u00d7768 (full window)\nProbe: active (96 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=tablet-landscape&run=r9-tablet-landscape__checkout&start=%2F%23shop', instruction_id='64adcf4d-092d-484c-84d2-be1d65497758'):
        await page.goto("http://localhost:4400/__ap/frame?profile=tablet-landscape&run=r9-tablet-landscape__checkout&start=%2F%23shop")
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Add to cart for Trail Runner Shoes', instruction_id='d0843634-3eb1-4df5-b98c-8d6fdd8602d9'):
        _loc_2 = frame_0.locator("internal:role=article >> internal:has-text=\"Trail Runner Shoes $129.00\"i >> internal:role=button")
        
        await _loc_2.click()
        # Reset to main page context
        frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Cart (1) in the header navigation', instruction_id='56c958b9-6356-4af7-8336-0ea9dbe70acb'):
        _loc_4 = frame_2.locator("internal:role=link[name=\"Cart (1)\"i]")
        
        await _loc_4.click()
        # Reset to main page context
    
    async with testmu.step('Waiting for the plan to be completed', instruction_id='e2641f02-9f9a-4b2d-aedb-18803e3f43f7'):
        await page.wait_for_timeout(1000)
        frame_4 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "2" into "Quantity for Trail Runner Shoes"', instruction_id='a814168d-50e5-4988-a539-6112090b0b28'):
        element_0 = frame_4.locator("internal:role=spinbutton[name=\"Quantity for Trail Runner\"i]")
        
        await testmu.fill(element_0, "2")
        # Reset to main page context
        frame_5 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Place order button', instruction_id='c32de027-9039-4238-900b-a4cd410425e9'):
        _loc_7 = frame_5.locator("internal:role=button[name=\"Place order\"i]")
        
        await _loc_7.click()
        # Reset to main page context
    _condition_met = False
    _until_retries = 0
    while _until_retries < 10:
        print(f"[until-loop] iteration {_until_retries + 1}/10")
        async with testmu.step('Waiting for the Order confirmed message to become visible', instruction_id='d3ee8c12-03d5-479d-a266-fc37d22c84ab'):
            await page.wait_for_timeout(500)
        await page.wait_for_timeout(500)
        if await testmu.check_until_condition(page, "the text 'Order confirmed' is visible"):
            _condition_met = True
            break
        _until_retries += 1
    set_var("__result__", {"condition_met": _condition_met, "retries": _until_retries + 1})
    
    async with testmu.step('Checking whether the order confirmation message is present'):
        set_var('order_confirmed_message', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {12: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(12).innerText.includes('Order confirmed'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Order confirmed! 2 items, $"i'], query="whether the 'Order confirmed' message is present in the order status area", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="an 'Order confirmed' message appears"))
    
    async with testmu.step('Assertion check', instruction_id='e9e99b80-1793-44a7-bc0c-80f64f1c0aa6'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "an 'Order confirmed' message appears", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{order_confirmed_message}}', 'store_key': 'order_confirmed_message', 'variable_refs': {'{{order_confirmed_message}}': 'true'}}], 'sub_checks': [{'description': "an 'Order confirmed' message appears", 'store_key': 'order_confirmed_message', 'expected_value': 'true', 'extracted_value': '{{order_confirmed_message}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "an 'Order confirmed' message appears"})
    
    async with testmu.step('Reading the session issue count from the AspectProof layout panel'):
        set_var('issues_seen_this_session', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {20: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(20).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['#ap-seen'], query='the Issues seen this session count in the AspectProof layout panel', expected_value='0', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the "AspectProof layout" panel shows "Issues seen this session: 0"'))
    
    async with testmu.step('Extracting the full AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {16: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(16).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the full panel text is stored as {{layout_report}}'))
    
    async with testmu.step('Assertion check', instruction_id='2b3a4035-8b72-43cf-ad3c-94bdd5d4ab9c'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'passed': True, 'operator': 'equals', 'transforms': ['strip'], 'json_path': None, 'expected': '0', 'extracted_value': '{{issues_seen_this_session}}', 'store_key': 'issues_seen_this_session', 'variable_refs': {'{{issues_seen_this_session}}': '0'}}], 'sub_checks': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'store_key': 'issues_seen_this_session', 'expected_value': '0', 'extracted_value': '{{issues_seen_this_session}}', 'operator': 'equals', 'transforms': ['strip']}], 'composite_operator': 'and', 'claim': 'the "AspectProof layout" panel shows "Issues seen this session: 0"'})


if __name__ == "__main__":
    testmu.run(test)