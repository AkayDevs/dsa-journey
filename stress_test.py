#!/usr/bin/env python3
import random
import time
import sys
import argparse
from typing import Any, Callable, List, Dict, Tuple, Optional
import traceback
from datetime import timedelta

class StressTest:
    def __init__(
        self,
        solution_func: Callable,
        reference_func: Optional[Callable] = None,
        test_count: int = 100,
        time_limit_ms: int = 1000,
        seed: Optional[int] = None,
        verbose: bool = False
    ):
        """
        Initialize the stress test environment.
        
        Args:
            solution_func: The optimized solution to test
            reference_func: The reference/naive solution to compare against (optional)
            test_count: Number of tests to run
            time_limit_ms: Time limit per test in milliseconds
            seed: Random seed for reproducibility
            verbose: Print detailed information for each test
        """
        self.solution_func = solution_func
        self.reference_func = reference_func
        self.test_count = test_count
        self.time_limit_ms = time_limit_ms
        self.seed = seed if seed is not None else random.randint(0, 10**9)
        self.verbose = verbose
        self.stats = {
            "passed": 0,
            "failed": 0,
            "time_exceeded": 0,
            "error": 0,
            "total_time_ms": 0
        }
        self.failed_tests = []
        
        # Set random seed for reproducibility
        random.seed(self.seed)
        
    def generate_test(self) -> Dict[str, Any]:
        """
        Generate a random test case. Override this method to create specific test cases.
        
        Returns:
            Dictionary containing test data
        """
        # Default implementation generates a random array
        # Override this method to create specific test patterns
        array_size = random.randint(1, 1000)
        array = [random.randint(-1000, 1000) for _ in range(array_size)]
        return {
            "array": array,
            # Add other test parameters as needed
        }
    
    def run_test(self, test_data: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
        """
        Run a single test case with the solution and reference implementations.
        
        Args:
            test_data: The test case data
            
        Returns:
            (success, result_data) tuple
        """
        result = {
            "test_data": test_data,
            "solution_result": None,
            "reference_result": None,
            "solution_time_ms": 0,
            "reference_time_ms": 0,
            "error": None
        }
        
        # Run solution implementation
        try:
            start_time = time.time()
            result["solution_result"] = self.solution_func(**test_data)
            end_time = time.time()
            result["solution_time_ms"] = (end_time - start_time) * 1000
        except Exception as e:
            result["error"] = f"Solution error: {str(e)}\n{traceback.format_exc()}"
            return False, result
            
        # Time limit check
        if result["solution_time_ms"] > self.time_limit_ms:
            return False, result
            
        # Run reference implementation if provided
        if self.reference_func:
            try:
                start_time = time.time()
                result["reference_result"] = self.reference_func(**test_data)
                end_time = time.time()
                result["reference_time_ms"] = (end_time - start_time) * 1000
                
                # Compare results
                if result["solution_result"] != result["reference_result"]:
                    return False, result
            except Exception as e:
                result["error"] = f"Reference error: {str(e)}\n{traceback.format_exc()}"
                return False, result
                
        return True, result
    
    def run_tests(self) -> Dict[str, Any]:
        """
        Run all test cases and collect statistics.
        
        Returns:
            Statistics dictionary
        """
        print(f"Running {self.test_count} tests with seed {self.seed}")
        print(f"Time limit per test: {self.time_limit_ms}ms")
        print("-" * 50)
        
        start_time = time.time()
        
        for i in range(1, self.test_count + 1):
            test_data = self.generate_test()
            success, result = self.run_test(test_data)
            
            if success:
                self.stats["passed"] += 1
                status = "✓ PASS"
            elif result["error"]:
                self.stats["error"] += 1
                status = "✗ ERROR"
                self.failed_tests.append(result)
            elif result["solution_time_ms"] > self.time_limit_ms:
                self.stats["time_exceeded"] += 1
                status = "⏱ TIME LIMIT"
                self.failed_tests.append(result)
            else:
                self.stats["failed"] += 1
                status = "✗ FAIL"
                self.failed_tests.append(result)
                
            self.stats["total_time_ms"] += result["solution_time_ms"]
            
            if self.verbose or not success:
                print(f"Test #{i}: {status} [{result['solution_time_ms']:.2f}ms]")
                if not success:
                    if result["error"]:
                        print(f"  Error: {result['error']}")
                    elif result["solution_time_ms"] > self.time_limit_ms:
                        print(f"  Time Limit Exceeded: {result['solution_time_ms']:.2f}ms > {self.time_limit_ms}ms")
                    else:
                        print(f"  Expected: {result['reference_result']}")
                        print(f"  Got: {result['solution_result']}")
                    print(f"  Test data: {self._format_test_data(result['test_data'])}")
                    print()
        
        end_time = time.time()
        total_time = end_time - start_time
        
        # Print summary
        print("\n" + "=" * 50)
        print(f"SUMMARY (Total time: {total_time:.2f}s)")
        print(f"Passed: {self.stats['passed']}/{self.test_count} ({self.stats['passed']/self.test_count*100:.1f}%)")
        print(f"Failed: {self.stats['failed']}/{self.test_count} ({self.stats['failed']/self.test_count*100:.1f}%)")
        print(f"Time Exceeded: {self.stats['time_exceeded']}/{self.test_count} ({self.stats['time_exceeded']/self.test_count*100:.1f}%)")
        print(f"Errors: {self.stats['error']}/{self.test_count} ({self.stats['error']/self.test_count*100:.1f}%)")
        print(f"Average time per test: {self.stats['total_time_ms']/self.test_count:.2f}ms")
        print("=" * 50)
        
        return self.stats
    
    def _format_test_data(self, test_data: Dict[str, Any]) -> str:
        """Format test data for display by shortening arrays and other large structures"""
        result = {}
        for key, value in test_data.items():
            if isinstance(value, list):
                if len(value) > 10:
                    result[key] = f"[{', '.join(str(x) for x in value[:5])}, ..., {', '.join(str(x) for x in value[-5:])}] (length: {len(value)})"
                else:
                    result[key] = value
            else:
                result[key] = value
        return str(result)
        
    def get_failed_tests(self) -> List[Dict[str, Any]]:
        """
        Get list of failed test cases.
        
        Returns:
            List of failed test dictionaries
        """
        return self.failed_tests


class ArrayStressTest(StressTest):
    """Specialized stress test for array-based problems"""
    
    def __init__(
        self,
        solution_func: Callable,
        reference_func: Optional[Callable] = None,
        test_count: int = 100,
        time_limit_ms: int = 1000,
        min_size: int = 1,
        max_size: int = 1000,
        min_value: int = -1000,
        max_value: int = 1000,
        seed: Optional[int] = None,
        verbose: bool = False
    ):
        super().__init__(solution_func, reference_func, test_count, time_limit_ms, seed, verbose)
        self.min_size = min_size
        self.max_size = max_size
        self.min_value = min_value
        self.max_value = max_value
        
    def generate_test(self) -> Dict[str, Any]:
        """Generate a random array test case"""
        array_size = random.randint(self.min_size, self.max_size)
        array = [random.randint(self.min_value, self.max_value) for _ in range(array_size)]
        return {"array": array}


class GraphStressTest(StressTest):
    """Specialized stress test for graph problems"""
    
    def __init__(
        self,
        solution_func: Callable,
        reference_func: Optional[Callable] = None,
        test_count: int = 100,
        time_limit_ms: int = 1000,
        min_nodes: int = 1,
        max_nodes: int = 100,
        directed: bool = False,
        weighted: bool = False,
        min_weight: int = 1,
        max_weight: int = 100,
        seed: Optional[int] = None,
        verbose: bool = False
    ):
        super().__init__(solution_func, reference_func, test_count, time_limit_ms, seed, verbose)
        self.min_nodes = min_nodes
        self.max_nodes = max_nodes
        self.directed = directed
        self.weighted = weighted
        self.min_weight = min_weight
        self.max_weight = max_weight
        
    def generate_test(self) -> Dict[str, Any]:
        """Generate a random graph test case"""
        num_nodes = random.randint(self.min_nodes, self.max_nodes)
        # Probability of edge existence - adjust to control graph density
        edge_prob = random.uniform(0.1, 0.3)
        
        if self.weighted:
            # Adjacency list with weights
            graph = [[] for _ in range(num_nodes)]
            edges = []
            
            for u in range(num_nodes):
                for v in range(num_nodes):
                    if u != v and random.random() < edge_prob:
                        weight = random.randint(self.min_weight, self.max_weight)
                        graph[u].append((v, weight))
                        edges.append((u, v, weight))
                        if not self.directed:
                            graph[v].append((u, weight))
        else:
            # Regular adjacency list
            graph = [[] for _ in range(num_nodes)]
            edges = []
            
            for u in range(num_nodes):
                for v in range(num_nodes):
                    if u != v and random.random() < edge_prob:
                        graph[u].append(v)
                        edges.append((u, v))
                        if not self.directed:
                            graph[v].append(u)
        
        return {
            "graph": graph,
            "num_nodes": num_nodes,
            "edges": edges
        }


class StringStressTest(StressTest):
    """Specialized stress test for string problems"""
    
    def __init__(
        self,
        solution_func: Callable,
        reference_func: Optional[Callable] = None,
        test_count: int = 100,
        time_limit_ms: int = 1000,
        min_length: int = 1,
        max_length: int = 1000,
        charset: str = "abcdefghijklmnopqrstuvwxyz",
        seed: Optional[int] = None,
        verbose: bool = False
    ):
        super().__init__(solution_func, reference_func, test_count, time_limit_ms, seed, verbose)
        self.min_length = min_length
        self.max_length = max_length
        self.charset = charset
        
    def generate_test(self) -> Dict[str, Any]:
        """Generate a random string test case"""
        length = random.randint(self.min_length, self.max_length)
        string = ''.join(random.choice(self.charset) for _ in range(length))
        return {"string": string}


# Example usage
def example():
    """Example showing how to use the stress test framework"""
    
    # Define the optimized solution
    def solution_sum(array):
        return sum(array)
    
    # Define the reference solution (intentionally incorrect for demo)
    def reference_sum(array):
        if len(array) == 0:
            return 0
        return array[0] + reference_sum(array[1:])
    
    # Run the stress test
    tester = ArrayStressTest(
        solution_func=solution_sum,
        reference_func=reference_sum,
        test_count=10,
        max_size=5,  # Small arrays to avoid recursion depth issues in the reference implementation
        verbose=True
    )
    tester.run_tests()
    
    print("\nFailed tests:")
    for failed_test in tester.get_failed_tests():
        print(failed_test)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DSA Solution Stress Tester")
    parser.add_argument("--example", action="store_true", help="Run example stress test")
    args = parser.parse_args()
    
    if args.example:
        example()
    else:
        print("Run with --example to see a demonstration") 