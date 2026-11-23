import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="88b5f5ec-353a-4a76-975b-5121015e51ac",
    name="Subscribe to Trail Notes and Verify Layout",
    tc_id="TC-73",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"subscribed_message_visible": "true", "issues_seen_this_session_zero": "true", "layout_report": "AspectProof layout\nTablet landscape 1024\u00d7768 (full window)\nProbe: active (97 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=tablet-landscape&run=r7-tablet-landscape__signup&start=%2F', instruction_id='c0d0365f-9afd-4373-b915-058404b5fec7'):
        await page.goto("http://localhost:4400/__ap/frame?profile=tablet-landscape&run=r7-tablet-landscape__signup&start=%2F")
    
    async with testmu.step('Waiting while the plan is queued and fields are being filled', instruction_id='8afeab36-57a4-4306-b669-975f32bf10c2'):
        await page.wait_for_timeout(1000)
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "Test User" into "Name"', instruction_id='b5e1acbb-e401-44f3-b737-13e3194d37b2'):
        element_0 = frame_0.locator("internal:role=textbox[name=\"Name\"i]")
        
        await testmu.fill(element_0, "Test User")
        # Reset to main page context
        frame_1 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Entering test@example.com in the Get trail notes form email field', instruction_id='07763763-b586-4b53-82ce-e6bc989f2c80'):
        element_1 = frame_1.locator("internal:role=textbox[name=\"Email\"i]")
        
        await testmu.fill(element_1, "test@example.com")
        # Reset to main page context
        frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Dismissing the promotion button', instruction_id='c5a6bbe5-c1a8-406d-9345-ad7d3a5af13a'):
        _loc_4 = frame_2.locator("internal:role=button[name=\"Dismiss promotion\"i]")
        
        await _loc_4.click()
        # Reset to main page context
        frame_4 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Subscribe button', instruction_id='82a782d0-223e-4bde-a74f-d568d5febc63'):
        _loc_6 = frame_4.locator("internal:role=button[name=\"Subscribe\"i]")
        
        await _loc_6.click()
        # Reset to main page context
    
    async with testmu.step('Checking whether the subscription confirmation message is present'):
        set_var('subscribed_message_visible', await testmu.textual_analyzer(page, wrapped_js='(els) => {\n  const __m = {23: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(23).innerText.includes("You\'re subscribed"));\n  return (typeof __v === \'boolean\' ? String(__v) : __v);\n}', locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Thanks, Test User! You\'re"i'], query="whether a 'You're subscribed' message is present in the subscription form status message", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="a 'You're subscribed' message appears"))
    
    async with testmu.step('Assertion check', instruction_id='92bedc20-eba7-4299-8b77-d00116e458b3'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "a 'You're subscribed' message appears", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{subscribed_message_visible}}', 'store_key': 'subscribed_message_visible', 'variable_refs': {'{{subscribed_message_visible}}': 'true'}}], 'sub_checks': [{'description': "a 'You're subscribed' message appears", 'store_key': 'subscribed_message_visible', 'expected_value': 'true', 'extracted_value': '{{subscribed_message_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "a 'You're subscribed' message appears"})
    
    async with testmu.step('Checking whether the session issues text is present'):
        set_var('issues_seen_this_session_zero', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {24: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(24).innerText.includes('Issues seen this session: 0'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='whether the "Issues seen this session: 0" text is present in the AspectProof layout panel', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the "AspectProof layout" panel shows "Issues seen this session: 0"'))
    
    async with testmu.step('Reading the AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {24: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(24).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the full "AspectProof layout" panel text is stored as {{layout_report}}'))
    
    async with testmu.step('Assertion check', instruction_id='91d1d3bf-b3a1-4fb8-9c50-517fcd8645e4'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{issues_seen_this_session_zero}}', 'store_key': 'issues_seen_this_session_zero', 'variable_refs': {'{{issues_seen_this_session_zero}}': 'true'}}], 'sub_checks': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'store_key': 'issues_seen_this_session_zero', 'expected_value': 'true', 'extracted_value': '{{issues_seen_this_session_zero}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the "AspectProof layout" panel shows "Issues seen this session: 0"'})


if __name__ == "__main__":
    testmu.run(test)