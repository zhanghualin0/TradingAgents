from .search_provider import (
    SearchProvider,
    GoogleSearchProvider,
    OpenAISearchProvider
)


class SearchProviderFactory:
    @staticmethod
    def create_provider(config: dict[str, any])->SearchProvider:
        backend_url = config["backend_url"]
        model = config["quick_think_llm"]

        if "generativelanguage.googleapis.com" in backend_url:
            return GoogleSearchProvider(model)
        else:
            return OpenAISearchProvider(model, backend_url)
        

