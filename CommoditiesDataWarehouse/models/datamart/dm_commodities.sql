with commodities as (
    select
        data, 
        ticker,
        valor_fechamento
    from
        {{ref('stg_commodities')}}

),

movimentacao as (
    select
        data,
        ticker,
        acao,
        quantidade
    from
        {{ref('stg_movimentacao_commodities')}}

),

joined as (
    select
        c.data,
        c.ticker,
        c.valor_fechamento,
        m.acao,
        m.quantidade,
        (m.quantidade * c.valor_fechamento) as valor,
        case
            when m.acao = 'sell'
            then (m.quantidade * c.valor_fechamento)
            else -(m.quantidade * c.valor_fechamento)
        end as ganho
    from
        commodities c
    inner join
        movimentacao m
    on
        c.data = m.data
        and c.ticker = m.ticker
),

last_day as (
    select
        max(data) as max_date
    from
        joined
),

filtered as (
    select
        *
    from
        joined
    where
        data = (select max_date from last_day)
)

select
    *
from
    filtered