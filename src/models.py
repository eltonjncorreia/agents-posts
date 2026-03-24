from pydantic import BaseModel
from typing import List, Optional


class SourceArticle(BaseModel):
    title: str
    url: str
    content: Optional[str]
    source: str
    published: Optional[str]


class ResearchResult(BaseModel):
    topic: str
    articles: List[SourceArticle]


class EditedArticle(BaseModel):
    title: str
    subtitle: Optional[str]
    content_html: str


class PublishResult(BaseModel):
    draft_id: str
    url: str
    status: str
