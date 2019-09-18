import collections
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AffinityPropagation
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import numpy as np
from cluster_visualization import ClusterVisualization

class SentenceClustering:
    def __init__(self, sents, nclusters,visualization=False):
        self.sents = sents
        self.nclusters = nclusters
        self.visualization = visualization

    def kmeans_clustering(self):
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform(self.sents)
        kmeans = KMeans(n_clusters=self.nclusters)
        kmeans.fit(tfidf_matrix)
        clusters = collections.defaultdict(list)
        for i, label in enumerate(kmeans.labels_):
            clusters[label].append(i)
        clus_viz = ClusterVisualization(tfidf_matrix)
        clus_viz.cluster_visualization_tsne()
        return dict(clusters)

    def affinity_clustering(self):
        tfidf_vectorizer = TfidfVectorizer()
        tf_idf_matrix = tfidf_vectorizer.fit_transform(self.sents)
        similarity_matrix = (tf_idf_matrix * tf_idf_matrix.T).A
        affinity_propagation = AffinityPropagation(affinity="precomputed",
                                                   damping=0.5)
        affinity_propagation.fit(similarity_matrix)
        clusters = collections.defaultdict(list)
        for i, label in enumerate(affinity_propagation.labels_):
            clusters[label].append(i)
        return dict(clusters)

    def Agglomerative_clustering(self):
        tfidf_vectorizer = TfidfVectorizer()
        tf_idf_matrix = tfidf_vectorizer.fit_transform(self.sents)
        similarity_matrix = (tf_idf_matrix * tf_idf_matrix.T).A
        agglomerativeclustering = AgglomerativeClustering()
        agglomerativeclustering.fit(similarity_matrix)
        clusters = collections.defaultdict(list)
        for i, label in enumerate(agglomerativeclustering.labels_):
            clusters[label].append(i)
        return dict(clusters)




