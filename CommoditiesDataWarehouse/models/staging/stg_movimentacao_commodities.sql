--import
with source as (
    select
        date,
        ticker,
        action,
        quantity
    from
        {{source ('dbcommodities', 'movimentacao_commodities')}}
),

--renamed
renamed as (
    select
        cast(date as date) as data,
        ticker as ticker,
        action as acao,
        quantity as quantidade
    from
        source
)
-- select * from
select * from renamed