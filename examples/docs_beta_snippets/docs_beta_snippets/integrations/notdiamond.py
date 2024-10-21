from dagster_notdiamond import NotDiamondResource

import dagster as dg


@dg.asset(compute_kind="NotDiamond")
def notdiamond_asset(context: dg.AssetExecutionContext, notdiamond: NotDiamondResource):
    with notdiamond.get_client(context) as client:
        client.chat.completions.create(
            model=["gpt-4o", "gpt-4o-mini"],
            messages=[{"role": "user", "content": "Say this is a test."}],
        )


notdiamond_asset_job = dg.define_asset_job(
    name="notdiamond_asset_job", selection="notdiamond_asset"
)

defs = dg.Definitions(
    assets=[notdiamond_asset],
    jobs=[notdiamond_asset_job],
    resources={
        "openai": NotDiamondResource(api_key=dg.EnvVar("OPENAI_API_KEY")),
    },
)
