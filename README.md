# Online Bookstore: Async PostgreSQL Search Optimization

## Task Overview
Your task involves improving the PostgreSQL integration for an online bookstore built on FastAPI. All routers, endpoints, and app scaffolding are already in place. Currently, book search endpoints—especially searching books by author and category—are much slower than expected as more data is added. Your focus will be on reviewing and improving the PostgreSQL schema (defining keys, indexes, and constraints), optimizing the search queries, and using correct async practices for database operations to speed up book retrievals based on author or category.

## Performance Issues
- Slow book search endpoints due to missing indexes on author and category fields
- Suboptimal table design: missing primary keys and constraints, redundant or inefficient data types
- Synchronous/blocking DB operations are causing bottlenecks in async routes
- No foreign key or relationship constraints between related entities
- Book lookups by author/category result in sequential scans instead of indexed access

## Database Access
- Host: `<DROPLET_IP>`
- Port: 5432
- Database: bookstore_db
- Username: store_user
- Password: store_pass
- You can use any PostgreSQL client (e.g., pgAdmin, DBeaver, psql) to connect and analyze/query the database
- Use EXPLAIN ANALYZE and query statistics to validate search/query performance

## Objectives
- Update the PostgreSQL schema: add indexes and constraints for efficient queries supporting book search requirements
- Refactor and implement async-compatible database logic for searching books by author or category (using asyncpg)
- Ensure all operations in FastAPI routes are non-blocking and efficient for both small and large datasets
- Test and validate that book lookups by author/category are significantly faster after your optimizations

## How to Verify
- Use search endpoints to retrieve books by author or category and observe reduced response times
- Analyze execution plans (`EXPLAIN ANALYZE`) to confirm index usage and faster access paths
- Confirm that background tasks or deferred operations (e.g., logging search activity) remain async-compatible
- Check that all schema changes (keys, indexes) do not break existing API functionality and are correctly enforced
