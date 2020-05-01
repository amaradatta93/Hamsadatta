import { TestBed } from '@angular/core/testing';

import { DashviewService } from './dashview.service';

describe('DashviewService', () => {
  let service: DashviewService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DashviewService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
