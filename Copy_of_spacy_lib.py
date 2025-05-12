{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM55wa2hHmpz6cJrmWCaMaX",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Monikarangasamy/NLP_spacy/blob/main/Copy_of_spacy_lib.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rhG7nKNdu7XA",
        "outputId": "a8d2a148-63b2-4281-b2fd-23e992f1c20e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: spacy in /usr/local/lib/python3.11/dist-packages (3.8.5)\n",
            "Requirement already satisfied: spacy-legacy<3.1.0,>=3.0.11 in /usr/local/lib/python3.11/dist-packages (from spacy) (3.0.12)\n",
            "Requirement already satisfied: spacy-loggers<2.0.0,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from spacy) (1.0.5)\n",
            "Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in /usr/local/lib/python3.11/dist-packages (from spacy) (1.0.12)\n",
            "Requirement already satisfied: cymem<2.1.0,>=2.0.2 in /usr/local/lib/python3.11/dist-packages (from spacy) (2.0.11)\n",
            "Requirement already satisfied: preshed<3.1.0,>=3.0.2 in /usr/local/lib/python3.11/dist-packages (from spacy) (3.0.9)\n",
            "Requirement already satisfied: thinc<8.4.0,>=8.3.4 in /usr/local/lib/python3.11/dist-packages (from spacy) (8.3.6)\n",
            "Requirement already satisfied: wasabi<1.2.0,>=0.9.1 in /usr/local/lib/python3.11/dist-packages (from spacy) (1.1.3)\n",
            "Requirement already satisfied: srsly<3.0.0,>=2.4.3 in /usr/local/lib/python3.11/dist-packages (from spacy) (2.5.1)\n",
            "Requirement already satisfied: catalogue<2.1.0,>=2.0.6 in /usr/local/lib/python3.11/dist-packages (from spacy) (2.0.10)\n",
            "Requirement already satisfied: weasel<0.5.0,>=0.1.0 in /usr/local/lib/python3.11/dist-packages (from spacy) (0.4.1)\n",
            "Requirement already satisfied: typer<1.0.0,>=0.3.0 in /usr/local/lib/python3.11/dist-packages (from spacy) (0.15.3)\n",
            "Requirement already satisfied: tqdm<5.0.0,>=4.38.0 in /usr/local/lib/python3.11/dist-packages (from spacy) (4.67.1)\n",
            "Requirement already satisfied: numpy>=1.19.0 in /usr/local/lib/python3.11/dist-packages (from spacy) (2.0.2)\n",
            "Requirement already satisfied: requests<3.0.0,>=2.13.0 in /usr/local/lib/python3.11/dist-packages (from spacy) (2.32.3)\n",
            "Requirement already satisfied: pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4 in /usr/local/lib/python3.11/dist-packages (from spacy) (2.11.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from spacy) (3.1.6)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.11/dist-packages (from spacy) (75.2.0)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.11/dist-packages (from spacy) (24.2)\n",
            "Requirement already satisfied: langcodes<4.0.0,>=3.2.0 in /usr/local/lib/python3.11/dist-packages (from spacy) (3.5.0)\n",
            "Requirement already satisfied: language-data>=1.2 in /usr/local/lib/python3.11/dist-packages (from langcodes<4.0.0,>=3.2.0->spacy) (1.3.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.33.2 in /usr/local/lib/python3.11/dist-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy) (2.33.2)\n",
            "Requirement already satisfied: typing-extensions>=4.12.2 in /usr/local/lib/python3.11/dist-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy) (4.13.2)\n",
            "Requirement already satisfied: typing-inspection>=0.4.0 in /usr/local/lib/python3.11/dist-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy) (0.4.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.13.0->spacy) (3.4.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.13.0->spacy) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.13.0->spacy) (2.4.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.13.0->spacy) (2025.4.26)\n",
            "Requirement already satisfied: blis<1.4.0,>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from thinc<8.4.0,>=8.3.4->spacy) (1.3.0)\n",
            "Requirement already satisfied: confection<1.0.0,>=0.0.1 in /usr/local/lib/python3.11/dist-packages (from thinc<8.4.0,>=8.3.4->spacy) (0.1.5)\n",
            "Requirement already satisfied: click>=8.0.0 in /usr/local/lib/python3.11/dist-packages (from typer<1.0.0,>=0.3.0->spacy) (8.1.8)\n",
            "Requirement already satisfied: shellingham>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from typer<1.0.0,>=0.3.0->spacy) (1.5.4)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.11/dist-packages (from typer<1.0.0,>=0.3.0->spacy) (13.9.4)\n",
            "Requirement already satisfied: cloudpathlib<1.0.0,>=0.7.0 in /usr/local/lib/python3.11/dist-packages (from weasel<0.5.0,>=0.1.0->spacy) (0.21.0)\n",
            "Requirement already satisfied: smart-open<8.0.0,>=5.2.1 in /usr/local/lib/python3.11/dist-packages (from weasel<0.5.0,>=0.1.0->spacy) (7.1.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->spacy) (3.0.2)\n",
            "Requirement already satisfied: marisa-trie>=1.1.0 in /usr/local/lib/python3.11/dist-packages (from language-data>=1.2->langcodes<4.0.0,>=3.2.0->spacy) (1.2.1)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.11/dist-packages (from rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.11/dist-packages (from rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy) (2.19.1)\n",
            "Requirement already satisfied: wrapt in /usr/local/lib/python3.11/dist-packages (from smart-open<8.0.0,>=5.2.1->weasel<0.5.0,>=0.1.0->spacy) (1.17.2)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.11/dist-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy) (0.1.2)\n"
          ]
        }
      ],
      "source": [
        "!pip install spacy"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import spacy"
      ],
      "metadata": {
        "id": "Koe_6D3bx3-l"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!python -m spacy download en_core_web_lg"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5qRwRLWhydPN",
        "outputId": "5cfcbbd2-ec21-4365-99b6-7be750d59593"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting en-core-web-lg==3.8.0\n",
            "  Downloading https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-3.8.0/en_core_web_lg-3.8.0-py3-none-any.whl (400.7 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m400.7/400.7 MB\u001b[0m \u001b[31m4.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: en-core-web-lg\n",
            "Successfully installed en-core-web-lg-3.8.0\n",
            "\u001b[38;5;2m✔ Download and installation successful\u001b[0m\n",
            "You can now load the package via spacy.load('en_core_web_lg')\n",
            "\u001b[38;5;3m⚠ Restart to reload dependencies\u001b[0m\n",
            "If you are in a Jupyter or Colab notebook, you may need to restart Python in\n",
            "order to load all the package's dependencies. You can do this by selecting the\n",
            "'Restart kernel' or 'Restart runtime' option.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "nlp=spacy.load('en_core_web_lg')"
      ],
      "metadata": {
        "id": "mk2zBAmly6UY"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "text=nlp('spacy is a library')"
      ],
      "metadata": {
        "id": "3VbQERpVzCVK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "1.Tokenization\n",
        "\n"
      ],
      "metadata": {
        "id": "1AlGwWxUzccY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "text\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9WjEHsPtzSgq",
        "outputId": "53451497-f607-49df-e929-6d369edf5ddf"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "spacy is a library"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for token in text:\n",
        "  print(token)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "brvRmJMWzUl4",
        "outputId": "889da7af-deb6-4a45-f898-cd56f72123ad"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "spacy\n",
            "is\n",
            "a\n",
            "library\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for token in text:\n",
        "  print(type(token))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rTpvuKDIzoZC",
        "outputId": "c57d8583-e8b2-4063-fb5a-cc3726ded137"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'spacy.tokens.token.Token'>\n",
            "<class 'spacy.tokens.token.Token'>\n",
            "<class 'spacy.tokens.token.Token'>\n",
            "<class 'spacy.tokens.token.Token'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for token in text:\n",
        "  print(type(token.text))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3nIwBB4zzuTN",
        "outputId": "36888121-3bf3-4934-b2f7-d426e02c77d4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'str'>\n",
            "<class 'str'>\n",
            "<class 'str'>\n",
            "<class 'str'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "text=nlp(\"The cost of the Iphone in U.K is 627$\")\n",
        "text"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UKzB8Olpz4lT",
        "outputId": "16747e2e-70d1-4f2d-ecf6-05ceb1d77797"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "The cost of the Iphone in U.K is 627$"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for token in text:\n",
        "  print(token)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "suJhzKAj0MIe",
        "outputId": "9b130148-0339-40ad-d585-5a14f7fa971f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The\n",
            "cost\n",
            "of\n",
            "the\n",
            "Iphone\n",
            "in\n",
            "U.K\n",
            "is\n",
            "627\n",
            "$\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "## 2.POS- part of speech\n",
        "for token in text:\n",
        "  print(token.text, token.pos)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_P_o_Q1_0jlr",
        "outputId": "82c99fd1-0370-4352-cc48-4c8f0dd90a59"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The 90\n",
            "cost 92\n",
            "of 85\n",
            "the 90\n",
            "Iphone 96\n",
            "in 85\n",
            "U.K 96\n",
            "is 87\n",
            "627 93\n",
            "$ 99\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "1aogjRcg0ZG_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for token in text:\n",
        "  print(token.text,token.pos_)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KHVeEeZo0hdM",
        "outputId": "ee601ef1-7e52-4e85-e07c-a87b3c244790"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The DET\n",
            "cost NOUN\n",
            "of ADP\n",
            "the DET\n",
            "Iphone PROPN\n",
            "in ADP\n",
            "U.K PROPN\n",
            "is AUX\n",
            "627 NUM\n",
            "$ SYM\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "### 3. Sentence Tokenization\n",
        "text=nlp('this is sentence one. this is sentence two. this is last now. lets study now')"
      ],
      "metadata": {
        "id": "cUc7NIgr08Fs"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "for sent in text:\n",
        "  print(sent)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qQEq7GZk1pOo",
        "outputId": "3b5ab7e3-0711-4070-face-b692c320249e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "this\n",
            "is\n",
            "sentence\n",
            "one\n",
            ".\n",
            "this\n",
            "is\n",
            "sentence\n",
            "two\n",
            ".\n",
            "this\n",
            "is\n",
            "last\n",
            "now\n",
            ".\n",
            "lets\n",
            "study\n",
            "now\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import nltk"
      ],
      "metadata": {
        "id": "yhK-tHSr17HI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from nltk.tokenize import sent_tokenize\n",
        "nltk.download('punkt')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2HtuMklG1_S2",
        "outputId": "0ca61a9c-07b2-434d-800a-1c5f872b30a8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "[nltk_data] Downloading package punkt to /root/nltk_data...\n",
            "[nltk_data]   Package punkt is already up-to-date!\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import nltk\n",
        "nltk.download('punkt_tab')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8IDMWcdk2h9y",
        "outputId": "9150d4cf-4d1a-4fcc-9608-024532f860e6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "[nltk_data] Downloading package punkt_tab to /root/nltk_data...\n",
            "[nltk_data]   Unzipping tokenizers/punkt_tab.zip.\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sent_tokenize('this is sentence one. this is sentence two. this is last now. lets study now')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "k5WrBGVG2ET1",
        "outputId": "71e6c21b-d717-4420-c667-6e1bb571ba76"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['this is sentence one.',\n",
              " 'this is sentence two.',\n",
              " 'this is last now.',\n",
              " 'lets study now']"
            ]
          },
          "metadata": {},
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from nltk.tokenize import word_tokenize\n",
        "nltk.download('punkt')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lQXTU96r23u3",
        "outputId": "4158352a-c6f0-4fc6-eebf-4f57458240ff"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "[nltk_data] Downloading package punkt to /root/nltk_data...\n",
            "[nltk_data]   Package punkt is already up-to-date!\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "word_tokenize('this is sentence one. this is sentence two. this is last now. lets study now')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qXwv2pa72q8R",
        "outputId": "94d2ef9d-a01e-46b4-9a60-f2d5271ca0d0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['this',\n",
              " 'is',\n",
              " 'sentence',\n",
              " 'one',\n",
              " '.',\n",
              " 'this',\n",
              " 'is',\n",
              " 'sentence',\n",
              " 'two',\n",
              " '.',\n",
              " 'this',\n",
              " 'is',\n",
              " 'last',\n",
              " 'now',\n",
              " '.',\n",
              " 'lets',\n",
              " 'study',\n",
              " 'now']"
            ]
          },
          "metadata": {},
          "execution_count": 34
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "'this is sentence one. this is sentence two. this is last now. lets study now'.split('.')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Iw06AzNp28dj",
        "outputId": "d8d51a75-9daa-476c-cf3a-73a49177adf4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['this is sentence one',\n",
              " ' this is sentence two',\n",
              " ' this is last now',\n",
              " ' lets study now']"
            ]
          },
          "metadata": {},
          "execution_count": 35
        }
      ]
    }
  ]
}