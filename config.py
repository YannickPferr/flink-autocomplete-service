# GPT configs
gpt_model = "text-davinci-003"
gpt_max_tokens = 64

# autocomplete configs
autocomplete_max_suggestions = 10

# scraper configs
scrape_url = "https://nightlies.apache.org/flink/flink-docs-master/"
scrape_pages_to_scrape = {'SQL': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/overview/', 'Getting Started': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/gettingstarted/', 'Overview': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/overview/', 'Hints': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/hints/', 'WITH clause': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/with/', 'SELECT & WHERE': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/select/', 'SELECT DISTINCT': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/select-distinct/', 'Windowing TVF': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/window-tvf/', 'Window Aggregation': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/window-agg/', 'Group Aggregation': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/group-agg/', 'Over Aggregation': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/over-agg/', 'Joins': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/joins/', 'Window JOIN': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/window-join/', 'Set Operations': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/set-ops/', 'ORDER BY clause': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/orderby/', 'LIMIT clause': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/limit/', 'Top-N': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/topn/', 'Window Top-N': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/window-topn/', 'Deduplication': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/deduplication/', 'Window Deduplication': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/window-deduplication/', 'Pattern Recognition': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/match_recognize/', 'CREATE Statements': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/create/', 'DROP Statements': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/drop/', 'ALTER Statements': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/alter/', 'INSERT Statement': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/insert/', 'ANALYZE Statements': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/analyze/', 'DESCRIBE Statements': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/describe/', 'EXPLAIN Statements': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/explain/', 'USE Statements': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/use/', 'SHOW Statements': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/show/', 'LOAD Statements': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/load/', 'UNLOAD Statements': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/unload/', 'SET Statements': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/set/', 'RESET Statements': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/reset/', 'JAR Statements': 'http://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/jar/'}