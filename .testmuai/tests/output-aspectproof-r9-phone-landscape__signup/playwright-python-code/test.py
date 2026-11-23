import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="8c47c6b6-4a4c-4b8a-8000-1f4cd8ed6af5",
    name="Subscribe to Trail Notes and Verify Layout Panel",
    tc_id="TC-86",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"youre_subscribed_message_visible": "true", "issues_seen_this_session_check": "true", "layout_report": "AspectProof layout\nPhone landscape 844\u00d7390 \u00b7 landscape\nProbe: active (72 scans)\nIssues now: 0\nIssues seen this session: 0", "layout_report_2": "AspectProof layout\nPhone landscape 844\u00d7390 \u00b7 landscape\nProbe: active (72 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=phone-landscape&run=r9-phone-landscape__signup&start=%2F', instruction_id='c5fc96fd-5930-48a7-aee6-cf731a235760'):
        await page.goto("http://localhost:4400/__ap/frame?profile=phone-landscape&run=r9-phone-landscape__signup&start=%2F")
    
    async with testmu.step('Waiting for queued plan steps to start', instruction_id='4bf187da-b1ce-428c-b023-d32028f0af68'):
        await page.wait_for_timeout(1000)
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "Test User" into "Name"', instruction_id='7021dc81-5e20-4484-9a6b-01c1738b9e50'):
        element_0 = frame_0.locator("internal:role=textbox[name=\"Name\"i]")
        
        await testmu.fill(element_0, "Test User")
        # Reset to main page context
        frame_1 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "test@example.com" into "Email"', instruction_id='348e41a0-71f1-4d94-9c24-1cbfa0bbda67'):
        element_1 = frame_1.locator("internal:role=textbox[name=\"Email\"i]")
        
        await testmu.fill(element_1, "test@example.com")
        # Reset to main page context
        frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Subscribe button', instruction_id='68a40de2-c162-4308-8d82-8433fd507639'):
        _loc_4 = frame_2.locator("internal:role=button[name=\"Subscribe\"i]")
        
        await _loc_4.click()
        # Reset to main page context
    
    async with testmu.step('Checking whether the subscription confirmation message is present'):
        set_var('youre_subscribed_message_visible', await testmu.textual_analyzer(page, wrapped_js='(els) => {\n  const __m = {23: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(23).innerText.includes("You\'re subscribed") && !!(el(23).offsetWidth || el(23).offsetHeight || el(23).getClientRects().length));\n  return (typeof __v === \'boolean\' ? String(__v) : __v);\n}', locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Thanks, Test User! You\'re"i'], query="whether a 'You're subscribed' message is visible in the subscription form status area", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="a 'You're subscribed' message appears"))
    
    async with testmu.step('Assertion check', instruction_id='c3a8f023-c791-477c-8add-2bcf292b22ba'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "a 'You're subscribed' message appears", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{youre_subscribed_message_visible}}', 'store_key': 'youre_subscribed_message_visible', 'variable_refs': {'{{youre_subscribed_message_visible}}': 'true'}}], 'sub_checks': [{'description': "a 'You're subscribed' message appears", 'store_key': 'youre_subscribed_message_visible', 'expected_value': 'true', 'extracted_value': '{{youre_subscribed_message_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "a 'You're subscribed' message appears"})
    
    async with testmu.step('Checking the session issue count in the AspectProof layout panel'):
        set_var('issues_seen_this_session_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {30: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(30).innerText.trim() === 'Issues seen this session: 0');\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Issues seen this session:"i'], query='whether the Issues seen this session line in the AspectProof layout panel displays 0', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the "AspectProof layout" panel shows "Issues seen this session: 0"'))
    
    async with testmu.step('Extracting the AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {27: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(27).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the full "AspectProof layout" panel text is stored as {{layout_report}}'))
    
    async with testmu.step('Extracting the AspectProof layout panel text'):
        set_var('layout_report_2', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {27: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(27).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the full AspectProof layout panel text is stored as {{layout_report}}', reprobe=True))
    
    async with testmu.step('Assertion check', instruction_id='f819762f-2f2f-4feb-8ffb-4823ac12711e'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{issues_seen_this_session_check}}', 'store_key': 'issues_seen_this_session_check', 'variable_refs': {'{{issues_seen_this_session_check}}': 'true'}}], 'sub_checks': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'store_key': 'issues_seen_this_session_check', 'expected_value': 'true', 'extracted_value': '{{issues_seen_this_session_check}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the "AspectProof layout" panel shows "Issues seen this session: 0"'})


if __name__ == "__main__":
    testmu.run(test)