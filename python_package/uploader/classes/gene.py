#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from named_individual import *
from superphy.uploader import _sparql

class Gene(NamedIndividual):
    """
    A gene with associated metadata

    """

    def __init__(self, graph, name, **kwargs):
        """
        Creates a Gene with associated metadata

        **kwargs is a dictionary of optional metadata used to pass them in

        Attributes:
            searchparam: list of keywords to filter kwargs by

        Args:
            graph (rdflib.Graph): container object to store RDF triples
            name (str): name of the Gene
            **kwargs (dict): optional arguments for Gene, that will be filtered for
                           spurious entries

        """

        searchparam = ["name", "reference_genome", "begin", "end", "vfo_id", "category", "sub_category", "uniprot"]

        super(Gene, self).__init__(graph, name)
        self.kwargs = {key: value for key, value in kwargs.items() if key in searchparam}

    def rdf(self):
        """
        Convert all Gene metadata to RDF and adds it to the graph

        As methods are called based on their keys, there is some coupling with minerJSON.py to
        ensure that the keys are properly named.
        """

        super(Gene, self).rdf()

        for key, value in self.kwargs.iteritems():
            getattr(self, key)(value)

        self.graph.add((n[self.name], rdf.type, gfvo.Gene))
        self.graph.add((n[self.name], rdf.type, faldo.Region))


    def reference_genome(self, reference_genome):
        """
        Adds a relationship between the gene and the reference genome it is from.

        Args:
            reference_genome: an accession number for the genome's URI
        """
        for item in reference_genome:
            node = _sparql.find_genome(item)
            self.graph.add((n[self.name], n.has_reference_genome, n[node]))



    def begin(self, begin):
        """
        Converts the start location to RDF and adds it to the graph

        Args:
            start: a string indicating the start of the reference gene.
        """

        literal = Literal(begin, datatype=XSD.string)
        begin_name = self.name + "_begin"
        self.graph.add((n[self.name], faldo.begin, n[begin_name]))
        self.graph.add((n[begin_name], rdf.type, faldo.Position))
        self.graph.add((n[begin_name], rdf.type, faldo.ExactPosition))
        self.graph.add((n[begin_name], rdf.type, faldo.ForwardStrandPosition))
        self.graph.add((n[begin_name], faldo.position, literal))

    def end(self, end):
        """
        Converts the stop location to RDF and adds it to the graph

        Args:
            start: a string indicating the start of the reference gene.
        """

        literal = Literal(end, datatype=XSD.string)
        end_name = self.name + "_end"
        self.graph.add((n[self.name], faldo.end, n[end_name]))
        self.graph.add((n[end_name], rdf.type, faldo.Position))
        self.graph.add((n[end_name], rdf.type, faldo.ExactPosition))
        self.graph.add((n[end_name], rdf.type, faldo.ForwardStrandPosition))
        self.graph.add((n[end_name], faldo.position, literal))

    def vfo_id(self, vfo_id):
        """
        Converts VFO ID into RDF and adds it to the graph

        Args:
            vfo_id(str): an id from VFDB
        """

        literal = Literal(vfo_id, datatype=XSD.string)
        self.graph.add((n[self.name], n.has_vfo_id, literal))

    def category(self, categories):
        """
        Converts the category to RDF and adds it to the graph

        Args:
            categories(str): list of categories that the gene belongs to
        """

        for item in categories:
            node = _sparql.find_category(item)
            self.graph.add((n[self.name], n.has_category, n[item]))

    def sub_category(self, sub_categories):
        """
        Converts all sub categories into RDF and adds it to the graph

        Args:
            sub_categories: list of sub categories that the gene belongs to
        """

        for item in sub_categories:
            node = _sparql.find_sub_category(item)
            self.graph.add((n[self.name], n.has_sub_category, n[item]))

    def uniprot(self, uniprot):
        """
        Converts Uniprot into RDF and adds it to the graph

        Args:
            uniprot(str): a Uniprot ID
        """

        literal = Literal(uniprot, datatype=XSD.string)
        self.graph.add((n[self.name], n.has_uniprot, literal))