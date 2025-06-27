import streamlit as st
from iam_fetcher import get_iam_users, get_user_policies, get_inline_policies, get_access_keys
from analyzer import is_key_old, has_admin_policy

st.set_page_config(page_title="IAM Analyzer", layout="wide")
st.title("🔐 AWS IAM Analyzer Dashboard")

users = get_iam_users()
st.success(f"✅ Total IAM Users: {len(users)}")

for user in users:
    username = user['UserName']
    st.subheader(f"👤 {username}")

    attached_policies = get_user_policies(username)
    inline_policies = get_inline_policies(username)
    keys = get_access_keys(username)

    policy_names = [p['PolicyName'] for p in attached_policies]
    st.write("📌 Attached Policies:", policy_names)
    if inline_policies:
        st.warning("⚠️ Has Inline Policies:")
        st.write(inline_policies)

    if has_admin_policy(attached_policies):
        st.error("🚨 This user has AdministratorAccess!")

    if not keys:
        st.info("No Access Keys")
    for key in keys:
        st.write(f"🔑 KeyID: `{key['AccessKeyId']}` - Status: `{key['Status']}`")
        if is_key_old(key):
            st.warning("🕒 Access key is older than 90 days!")
