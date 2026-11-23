import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="8b577a52-7bb2-4ead-a1c2-626a7b32ac78",
    name="Add and Order Trail Runner Shoes",
    tc_id="TC-9",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"order_confirmed_message": "true", "issues_seen_this_session": "true", "layout_report": "AspectProof layout\nLaptop 1280\u00d7800 (full window)\nProbe: active (88 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=laptop-1280&run=r3-laptop-1280__checkout&start=%2F%23shop', instruction_id='d275a8c6-d511-4e65-89cc-45b18a2b3b52'):
        await page.goto("http://localhost:4400/__ap/frame?profile=laptop-1280&run=r3-laptop-1280__checkout&start=%2F%23shop")
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Add to cart for Trail Runner Shoes', instruction_id='80901cbd-5375-4db1-b2cf-5d625afe6eec'):
        _loc_2 = frame_0.locator("internal:role=article >> internal:has-text=\"Trail Runner Shoes $129.00\"i >> internal:role=button")
        
        await _loc_2.click()
        # Reset to main page context
        frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Cart (1) in the header navigation', instruction_id='5753bbfb-33c3-44c1-b523-25f8e85dce52'):
        _loc_4 = frame_2.locator("internal:role=link[name=\"Cart (1)\"i]")
        
        await _loc_4.click()
        # Reset to main page context
        frame_4 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Typing 2 into Trail Runner Shoes quantity field', instruction_id='b7849a77-5a4c-4bc5-8bf1-47aa42952322'):
        element_0 = frame_4.locator("internal:role=spinbutton[name=\"Quantity for Trail Runner\"i]")
        
        await testmu.fill(element_0, "2")
        # Reset to main page context
        frame_5 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Place order', instruction_id='8d7be2eb-3143-44dc-8dbb-f357b0cdb8b5'):
        _loc_7 = frame_5.locator("internal:role=button[name=\"Place order\"i]")
        
        await _loc_7.click()
        # Reset to main page context
    
    async with testmu.step('Checking whether the order confirmation message is present'):
        set_var('order_confirmed_message', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {12: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(12).innerText.includes('Order confirmed'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Order confirmed! 2 items, $"i'], query="whether the 'Order confirmed' message is present in the order status area", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="an 'Order confirmed' message appears"))
    
    async with testmu.step('Assertion check', instruction_id='e5cc13bc-6d93-4b97-a919-180a5a6361e9'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "an 'Order confirmed' message appears", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{order_confirmed_message}}', 'store_key': 'order_confirmed_message', 'variable_refs': {'{{order_confirmed_message}}': 'true'}}], 'sub_checks': [{'description': "an 'Order confirmed' message appears", 'store_key': 'order_confirmed_message', 'expected_value': 'true', 'extracted_value': '{{order_confirmed_message}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "an 'Order confirmed' message appears"})
    
    async with testmu.step('Checking whether the session issue count is present'):
        set_var('issues_seen_this_session', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {16: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (/Issues seen this session:\\s*0/.test(el(16).innerText));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='whether the text "Issues seen this session: 0" is present in the AspectProof layout panel', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the "AspectProof layout" panel shows "Issues seen this session: 0"'))
    
    async with testmu.step('Reading the AspectProof layout panel report'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {16: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(16).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the full panel text is stored as {{layout_report}}'))
    
    async with testmu.step('Assertion check', instruction_id='bb616f5e-67db-4748-a05c-516773f692b9'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{issues_seen_this_session}}', 'store_key': 'issues_seen_this_session', 'variable_refs': {'{{issues_seen_this_session}}': 'true'}}], 'sub_checks': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'store_key': 'issues_seen_this_session', 'expected_value': 'true', 'extracted_value': '{{issues_seen_this_session}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the "AspectProof layout" panel shows "Issues seen this session: 0"'})


if __name__ == "__main__":
    testmu.run(test)