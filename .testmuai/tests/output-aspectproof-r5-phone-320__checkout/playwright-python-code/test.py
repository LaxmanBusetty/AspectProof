import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="688f577a-8403-48f1-87e2-b49bd82496d8",
    name="Add and Order Trail Runner Shoes on Mobile",
    tc_id="TC-48",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"cart_links_visible": "false", "order_confirmed_message_visible": "true", "issues_seen_this_session_zero": "true", "layout_report": "AspectProof layout\nPhone 320\u00d7568 (small Android) \u00b7 portrait\nProbe: active (110 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=phone-320&run=r5-phone-320__checkout&start=%2F%23shop', instruction_id='6f693caa-a629-4e94-bfed-4eb4041a6e4e'):
        await page.goto("http://localhost:4400/__ap/frame?profile=phone-320&run=r5-phone-320__checkout&start=%2F%23shop")
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Add to cart for Trail Runner Shoes', instruction_id='cdebaaca-1dc7-4abe-aed6-b0a8c91db9d4'):
        _loc_2 = frame_0.locator("internal:role=article >> internal:has-text=\"Trail Runner Shoes $129.00\"i >> internal:role=button")
        
        await _loc_2.click()
        # Reset to main page context
    
    async with testmu.step('whether the cart links are visible in the page header navigation', instruction_id='33d9a7e9-689b-491d-9041-a84073ee5765'):
        set_var('cart_links_visible', await testmu.vision_query(page, "whether the cart links are visible in the page header navigation", ""))
    if await testmu.evaluate_branch(sub_checks=[{'description': 'the cart links are not visible', 'store_key': 'cart_links_visible', 'expected_value': 'false', 'stored_value': '{{cart_links_visible}}', 'extracted_value': '{{cart_links_visible}}', 'operator': 'equals', 'transforms': []}], composite_operator="and"):
        frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
        
        async with testmu.step('Clicking the Menu button in the top-right header', instruction_id='82dcc952-a88d-463e-8e70-21745849dc52'):
            _loc_4 = frame_2.locator("internal:role=button[name=\"Menu\"i]")
            
            await _loc_4.click()
            # Reset to main page context
    frame_4 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking the Cart (1) link in the header navigation', instruction_id='4c790730-8a05-4e46-b558-64a36a84a3b4'):
        _loc_6 = frame_4.locator("internal:role=link[name=\"Cart (1)\"i]")
        
        await _loc_6.click()
        # Reset to main page context
    
    async with testmu.step('Waiting for the order to be placed', instruction_id='c7c1123e-dc4a-4fb6-bc22-731e4961bcbe'):
        await page.wait_for_timeout(1000)
        frame_6 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "2" into "Quantity for Trail Runner Shoes"', instruction_id='5632c26e-d15d-41d9-81fc-c214e8d22cd2'):
        element_0 = frame_6.locator("internal:role=spinbutton[name=\"Quantity for Trail Runner\"i]")
        
        await testmu.fill(element_0, "2")
        # Reset to main page context
        frame_7 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Click "Place order"', instruction_id='0c529741-e873-4fa0-853f-5f394b37650e'):
        _loc_9 = frame_7.locator("internal:role=button[name=\"Place order\"i]")
        
        await _loc_9.click()
        # Reset to main page context
    
    async with testmu.step('Checking whether the order confirmation message is present'):
        set_var('order_confirmed_message_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {9: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(9).innerText.includes('Order confirmed'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Order confirmed! 2 items, $"i'], query="whether an 'Order confirmed' message is present in the order status region", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="An 'Order confirmed' message appears."))
    
    async with testmu.step('Checking the issues seen count in the layout panel'):
        set_var('issues_seen_this_session_zero', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {16: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(16).innerText.trim() === 'Issues seen this session: 0');\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Issues seen this session:"i'], query="whether the 'Issues seen this session: 0' text is present in the AspectProof layout panel", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='The "AspectProof layout" panel shows "Issues seen this session: 0".'))
    
    async with testmu.step('Extracting the full layout panel report'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {13: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(13).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The full panel text is stored as {{layout_report}}.'))
    
    async with testmu.step('Assertion check', instruction_id='1cf29551-55b9-4c6b-8dbf-d59fe5a25139'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "An 'Order confirmed' message appears.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{order_confirmed_message_visible}}', 'store_key': 'order_confirmed_message_visible', 'variable_refs': {'{{order_confirmed_message_visible}}': 'true'}}], 'sub_checks': [{'description': "An 'Order confirmed' message appears.", 'store_key': 'order_confirmed_message_visible', 'expected_value': 'true', 'extracted_value': '{{order_confirmed_message_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "An 'Order confirmed' message appears."})
    
    async with testmu.step('Assertion check', instruction_id='714bb30d-fb8e-471e-9ab3-f97856dd762e'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{issues_seen_this_session_zero}}', 'store_key': 'issues_seen_this_session_zero', 'variable_refs': {'{{issues_seen_this_session_zero}}': 'true'}}], 'sub_checks': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'store_key': 'issues_seen_this_session_zero', 'expected_value': 'true', 'extracted_value': '{{issues_seen_this_session_zero}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'The "AspectProof layout" panel shows "Issues seen this session: 0".'})


if __name__ == "__main__":
    testmu.run(test)