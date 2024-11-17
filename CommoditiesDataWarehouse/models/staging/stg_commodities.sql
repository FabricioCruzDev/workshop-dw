-- import
with source as (
    select
        "Date",
        "Close",
        "ticker_id"
    from
        {{source ('dbcommodities', 'commodities')}}
),

--renamed
renamed as (
    select
        cast("Date" as date) as data,
        "Close" as valor_fechamento,
        "ticker_id" as Ticker
    from
        source
)
-- select * from
select * from renamed