from typing import Any, List

from articles.v1.daos import ArticleDAO
from esmerald import AsyncDAOProtocol
from posts.models import Post
from saffier import ObjectNotFound

from .schemas import Error, PostOut


class PostDAO(AsyncDAOProtocol):
    model: Post = Post

    async def get_all(self, **kwargs: Any) -> List[PostOut]:
        article_id = kwargs.get("article_id")
        article_dao = ArticleDAO()

        article = await article_dao.get(article_id)

        posts: List[Post] = await self.model.query.filter(article__id=article.id)
        posts_out: List[PostOut] = []

        for post in posts:
            await post.user.load()
            posts_out.append(
                PostOut(
                    id=post.pk,
                    content=post.content,
                    user=post.user.username,
                    created_at=str(post.created_at),
                )
                for post in posts
            )
        return posts_out
